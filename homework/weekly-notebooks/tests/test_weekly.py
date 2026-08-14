"""Completion check for the weekly in-class notebooks.

    python3 tests/test_weekly.py        # no pytest needed
    pytest tests/test_weekly.py         # if you have it

One check per week. Early in the term most of them will say "not yet
submitted" — that is not a failure, it is the term not having happened yet. By
the end, every week should be green.

Nothing here looks at whether your answers are right. It looks at whether you
worked through the notebook: that it is committed, that it ran, and that no
cell was left sitting on an error.

Deps: the standard library. It never runs your notebooks.

GENERATED FILE — do not edit. Source: tools/weekly_template.py, copied by
tools/build_weekly_manifest.py. Fix bugs in the template, not here.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = Path(__file__).resolve().parent / "manifest.json"


def _spec() -> dict:
    return json.loads(MANIFEST.read_text())


def find(name: str) -> Path | None:
    """Locate a notebook by filename, anywhere in the repo.

    Globbed rather than fixed to a path so that keeping your weeks in folders,
    or not, is up to you.
    """
    direct = ROOT / name
    if direct.exists():
        return direct
    hits = [p for p in ROOT.rglob(name) if ".ipynb_checkpoints" not in p.parts]
    return sorted(hits)[0] if hits else None


def inspect(path: Path, starter_cells: int) -> tuple[float, list[str]]:
    """Return (fraction of starter cells executed, problems)."""
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        return 0.0, [f"{path.name} is not readable as a notebook ({exc})"]

    code = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]
    problems = []
    for i, cell in enumerate(code):
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                problems.append(
                    f"{path.name} cell {i + 1} ended in "
                    f"{out.get('ename', 'an error')} — re-run it before committing")

    ran = sum(1 for c in code if c.get("execution_count") is not None)
    if starter_cells <= 0:
        return 1.0, problems
    return min(ran / starter_cells, 1.0), problems


def check_week(week: dict, threshold: float) -> tuple[bool, list[str]]:
    """(complete, messages) for one week."""
    msgs, done = [], True
    for entry in week["notebooks"]:
        path = find(entry["name"])
        if path is None:
            msgs.append(f"{entry['name']} — not yet submitted")
            done = False
            continue
        if entry.get("informational"):
            msgs.append(f"{entry['name']} — present (nothing to run)")
            continue
        frac, problems = inspect(path, entry["code_cells"])
        msgs += problems
        if problems:
            done = False
        if frac + 1e-9 < threshold:
            msgs.append(f"{entry['name']} — {frac:.0%} of cells run, "
                        f"{threshold:.0%} needed")
            done = False
        else:
            msgs.append(f"{entry['name']} — {frac:.0%} run ✓")
    return done, msgs


def summary() -> tuple[int, int, list[str]]:
    spec = _spec()
    t = spec["threshold"]
    done, lines = 0, []
    for week in spec["weeks"]:
        ok, msgs = check_week(week, t)
        done += ok
        lines.append(f"{week['week']}: {'complete' if ok else 'incomplete'}")
        lines += [f"    {m}" for m in msgs]
    return done, len(spec["weeks"]), lines


# --- one test per week, so progress is legible rather than all-or-nothing ---

def _make(week: dict, threshold: float):
    def test():
        ok, msgs = check_week(week, threshold)
        assert ok, f"{week['week']} is not complete yet:\n  " + "\n  ".join(msgs)
    test.__name__ = f"test_{week['week'].replace('-', '_')}"
    test.__doc__ = f"{week['week']} notebooks worked through"
    return test


CHECKS = []
for _w in _spec()["weeks"]:
    _t = _make(_w, _spec()["threshold"])
    globals()[_t.__name__] = _t          # pytest collects these
    CHECKS.append(_t)


def main() -> int:
    done, total, lines = summary()
    for line in lines:
        print(line)
    print(f"\n{done}/{total} weeks complete")
    if done < total:
        print("Weeks you have not reached yet are expected to be incomplete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
