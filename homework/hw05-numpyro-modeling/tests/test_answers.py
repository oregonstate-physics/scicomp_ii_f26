"""Automatic checks for this assignment. Runs in CI on every push; run it yourself too.

    python3 tests/test_answers.py       # no pytest needed
    pytest tests/test_answers.py        # if you have it

Two things are checked, and neither is your code:

  completion  -- a notebook is committed, it has been run, and no cell ended in
                 an error. Cells run out of order produce a warning, never a
                 failure.
  answers     -- each number in answers.json lands in a plausible range.

Most ranges are stored as hashes rather than as numbers. That is not a serious
lock -- a short script inverts it -- and it is not meant to be one. It is there
so the expected answers are not simply sitting in front of you while you work.
Typing in a number you did not compute will pass this file and will be obvious
in your write-up, which is where the marks are.

Some checks compare two of your own answers against each other rather than
against a stored value. Those are exact relationships that hold for any correct
sample, so there is nothing to hide.

Deps: the standard library. Nothing here imports numpy, and it never runs your
notebook.

GENERATED FILE -- do not edit. Source: tools/grader_template.py, copied into each
assignment by tools/build_grader.py. Fix bugs in the template, not here.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = Path(__file__).resolve().parent / "expected.json"


# --- locating the student's files -------------------------------------------
# Glob rather than hard-code: a renamed notebook should not read as a zero.

def find_answers() -> Path | None:
    direct = ROOT / "answers.json"
    if direct.exists():
        return direct
    hits = sorted(ROOT.rglob("answers.json"))
    return hits[0] if hits else None


def find_notebooks() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.ipynb")
                  if ".ipynb_checkpoints" not in p.parts)


# --- the banded-hash comparison ---------------------------------------------

def _bucket(value: float, width: float) -> int:
    return math.floor(value / width)


def _digest(key: str, bucket: int) -> str:
    return hashlib.sha256(f"{key}|{bucket}".encode()).hexdigest()[:16]


OPS = {
    "identity": lambda v: v,
    "log10": lambda v: math.log10(v) if v > 0 else float("nan"),
}


def check_value(key: str, value: float, rule: dict) -> str | None:
    """Return None if the value is acceptable, else a message saying why not."""
    if not math.isfinite(value):
        return f"{key} is {value}, not a finite number"

    kind = rule["kind"]
    if kind == "min":
        if value < rule["value"]:
            return (f"{key} = {value:g}, but the assignment asks for at least "
                    f"{rule['value']:g}")
        return None

    if kind == "banded":
        if _digest(key, _bucket(value, rule["width"])) in rule["digests"]:
            return None
        return (f"{key} = {value:.6g} is outside the accepted range. "
                + rule.get("hint", "Check that the quantity you recorded is the "
                                    "one being asked for."))

    return f"expected.json has an unknown rule kind {kind!r} for {key}"


def check_relation(rule: dict, answers: dict) -> str | None:
    """Compare two of the student's own answers. No stored value involved."""
    left, right = rule["left"], rule["right"]
    for k in (left, right):
        if k not in answers:
            return f"{k} was never recorded, so {rule['describes']} cannot be checked"
    try:
        a = float(answers[left])
        b = OPS[rule["op"]](float(answers[right]))
    except (TypeError, ValueError, KeyError):
        return f"{left} or {right} is not a number"
    if not (math.isfinite(a) and math.isfinite(b)):
        return f"{left} or {right} is not finite"

    if abs(a - b) <= rule["atol"] + rule["rtol"] * abs(b):
        return None
    return (f"{rule['describes']}: {left} = {a:.10g} but {rule['op']}({right}) "
            f"= {b:.10g}. " + rule.get("hint", ""))


# --- notebook completion (static inspection, never execution) ---------------

def inspect_notebook(path: Path) -> tuple[list[str], list[str], bool]:
    """Return (failures, warnings, shows_work) for one notebook.

    `shows_work` means the notebook has code cells that have been run. A
    notebook with no code cells is not a failure -- some assignments ship the
    questions as a markdown-only notebook -- it simply is not evidence.
    """
    fails: list[str] = []
    warns: list[str] = []
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [f"{path.name} is not readable as a notebook ({exc})"], [], False

    code = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]

    for i, cell in enumerate(code):
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                name = out.get("ename", "error")
                fails.append(f"{path.name} code cell {i + 1} ended in {name} -- "
                             "fix it and re-run before committing")

    ran = [c for c in code if c.get("execution_count") is not None]
    if ran:
        counts = [c["execution_count"] for c in ran]
        if counts != sorted(counts):
            warns.append(f"{path.name}: cells were run out of order. Not a problem, "
                         "but Restart & Run All before you commit makes the notebook "
                         "easier to follow.")
    return fails, warns, bool(ran)


# --- the checks themselves --------------------------------------------------

def _spec() -> dict:
    return json.loads(EXPECTED.read_text())


def _read_answers() -> dict:
    path = find_answers()
    return json.loads(path.read_text()) if path else {}


def test_notebook_committed():
    """At least one notebook must contain code that has been run.

    Not simply "an .ipynb exists": some assignments ship the questions as a
    markdown-only notebook, which would satisfy that without the student having
    committed anything.
    """
    nbs = find_notebooks()
    assert nbs, ("No .ipynb found. Commit the notebook you did the work in, "
                 "at the top level of this repository.")
    worked = [nb for nb in nbs if inspect_notebook(nb)[2]]
    assert worked, (
        "No notebook here has code cells that have been run. Commit the "
        "notebook you did the work in, after running it top to bottom. "
        f"Found: {', '.join(nb.name for nb in nbs)}")


def test_notebook_ran_cleanly():
    fails, warns = [], []
    for nb in find_notebooks():
        f, w, _ = inspect_notebook(nb)
        fails += f
        warns += w
    for w in warns:
        print(f"warning: {w}")
    assert not fails, "\n".join(fails)


def test_answers_file_present():
    path = find_answers()
    assert path is not None, (
        "No answers.json. Use submit.answer(...) in your notebook to record each "
        "result, then commit the answers.json it writes.")
    data = json.loads(path.read_text())
    missing = sorted(set(_spec()["keys"]) - set(data))
    assert not missing, "answers.json is missing: " + ", ".join(missing)


def test_answers_in_range():
    path = find_answers()
    assert path is not None, "No answers.json -- see the previous check."
    data = json.loads(path.read_text())
    problems = []
    for key, rule in _spec()["keys"].items():
        if key not in data:
            problems.append(f"{key} was never recorded")
            continue
        try:
            value = float(data[key])
        except (TypeError, ValueError):
            problems.append(f"{key} is not a number")
            continue
        msg = check_value(key, value, rule)
        if msg:
            problems.append(msg)
    assert not problems, "\n".join(problems)


def test_relationships_hold():
    """Exact relationships between your own answers -- these hold for any correct
    sample, so failing one means a genuine mistake, not bad luck."""
    rules = _spec().get("relations", [])
    if not rules:
        return
    data = _read_answers()
    assert data, "No answers.json -- see the earlier check."
    problems = [m for m in (check_relation(r, data) for r in rules) if m]
    assert not problems, "\n".join(problems)


CHECKS = [test_notebook_committed, test_notebook_ran_cleanly,
          test_answers_file_present, test_answers_in_range,
          test_relationships_hold]


def main() -> int:
    failed = 0
    for check in CHECKS:
        try:
            check()
        except AssertionError as exc:
            failed += 1
            print(f"FAIL  {check.__name__}\n      "
                  + str(exc).replace("\n", "\n      "))
        else:
            print(f"ok    {check.__name__}")
    print(f"\n{len(CHECKS) - failed}/{len(CHECKS)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
