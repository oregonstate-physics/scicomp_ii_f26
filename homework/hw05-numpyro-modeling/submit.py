"""Record your answers so they can be checked automatically.

Put this line next to each result you are asked to report:

    import submit
    submit.answer("mean_rejection", my_sample_mean)

That writes (or updates) `answers.json` in this folder. Commit that file along
with your notebook -- it is what the checker reads.

`submit.show()` prints everything recorded so far, and
`submit.clear()` starts over.

Recording an answer is not the same as being right, and being right is a small
part of the grade. The checker looks at whether the number is in a plausible
range; the reasoning is assessed from your notebook and write-up.

GENERATED FILE -- do not edit. Source: tools/submit_template.py, copied into each
assignment by tools/build_grader.py.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

PATH = Path(__file__).resolve().parent / "answers.json"


def _load() -> dict:
    if not PATH.exists():
        return {}
    try:
        data = json.loads(PATH.read_text())
    except json.JSONDecodeError:
        raise SystemExit(
            f"{PATH.name} is not valid JSON. Delete it and re-run your notebook."
        )
    return data if isinstance(data, dict) else {}


def answer(key: str, value) -> None:
    """Record `value` under `key`. Overwrites any earlier value for that key."""
    if not isinstance(key, str) or not key:
        raise TypeError("key must be a non-empty string")

    # numpy scalars and 0-d arrays arrive here constantly; take the float.
    try:
        value = float(value)
    except (TypeError, ValueError):
        raise TypeError(
            f"answer({key!r}, ...) needs a single number, got {type(value).__name__}. "
            "If you have an array, pass the summary statistic itself "
            "(e.g. samples.mean(), not samples)."
        )
    if not math.isfinite(value):
        raise ValueError(
            f"answer({key!r}, {value}) is not a finite number -- something upstream "
            "produced inf or nan."
        )

    data = _load()
    data[key] = value
    PATH.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n")
    print(f"recorded {key} = {value:.6g}")


def show() -> dict:
    """Print and return everything recorded so far."""
    data = _load()
    if not data:
        print("nothing recorded yet")
    for k, v in sorted(data.items()):
        print(f"  {k:18s} {v:.6g}")
    return data


def clear() -> None:
    """Delete all recorded answers."""
    PATH.unlink(missing_ok=True)
    print("answers cleared")
