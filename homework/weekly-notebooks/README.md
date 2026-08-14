# Weekly notebooks

This is not a homework. It is the repository where your **in-class notebooks** live for
the whole term — one repo, added to each week, rather than a new submission every time.

It is worth **10% of your grade**, and it is checked for *completion only*. Nobody is
looking at whether your answers are right. What is being asked is that you worked through
the material.

## What to do each week

1. Get that week's notebook(s) from the class repository.
2. **Copy them into this repository** before you start editing. Work on the copy.
3. Work through them — in class, and finish afterwards if you ran out of time.
4. Commit and push.

You can arrange the files however you like. Keep the filenames as they are, but put them
in `week-03/` folders or leave them all at the top level — the checker searches the whole
repository by filename.

## What is checked

Run it yourself any time:

```
python3 tests/test_weekly.py
```

There is one check per week. For each notebook it asks three things:

- **Is it here?**
- **Was it run?** Specifically, has at least **half** of the notebook's code cells been
  executed. The denominator is the number of cells in *the version you were given*, so
  cells you add yourself can only ever help — experiment freely.
- **Did anything end in an error?** A cell left sitting on a traceback counts as not
  done. Re-run it before you commit.

A notebook with no code cells at all just needs to be present.

### Half, not all

Half is deliberate. Some cells take a long time, some need data you may not have on the
day, and some are there to be read rather than run. Working through most of a notebook is
what is being asked for; there are no extra marks for the last cell.

### Early in the term, most weeks will show as incomplete

That is the term not having happened yet, not a problem with your work. Week 7 cannot be
complete in week 3. What matters is the state at the end.

## A warning worth reading once

**Do not set up `nbstripout`, or any git filter that clears notebook outputs.** It is
sometimes recommended for keeping repositories tidy. Here it would silently erase the
execution counts and outputs on every commit — which is exactly the evidence this check
looks for — and your work would read as never having been run.
