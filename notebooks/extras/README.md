# Extras — not currently on the schedule

Notebooks that belong to the course but were not taught in the most recent
offering.  They live here rather than in a `week-NN/` folder so the week folders
stay an honest record of what is actually taught.

## `boltzmann-ising-metropolis.ipynb`

The Boltzmann distribution and a 2-D Ising model, used to motivate Markov chains
and the Metropolis algorithm before applying it to inference.  Historically this
came just before the Metropolis homework (week 3–4).

Reviewed 2026-08-06 and **left here deliberately.** Metropolis is already taught in
week 3 (`01-intro-to-sampling`), so this is a second implementation of the same
algorithm — it adds statistical-mechanics motivation and a 2-D lattice, but no new
method. It is also a *simulation*, not physics *data*, so it does nothing to reduce the
course's reliance on astronomical datasets.

## `logistic-regression-sdss.ipynb`

Identifying quasars in the Sloan Digital Sky Survey by logistic regression on photometric
colours. Was the second week-07 notebook until 2026-08-06, when it was replaced by the
superconductivity introduction that now feeds the final project.

Nothing wrong with it — it is a clean application of the method to real data, and a good
alternative if the condensed-matter thread is ever dropped. Its data
(`SDSS_stars.csv`, `SDSS_wd.csv`, `SDSS_quasar.dat`) is still in the top-level `data/`, and
its relative paths resolve unchanged from here.

## `gw-posterior-pdf.ipynb`

Inferring black hole properties from a gravitational-wave observation by
evaluating a posterior on a grid.  A natural capstone to the signal-processing
week (it follows the LIGO notebook) and a callback to the Bayesian inference
weeks.

## Restoring one

Move it into the appropriate `week-NN/` folder, renumber it into that week's
sequence, and add it to the week's section in the top-level `README.md`.
Check its relative paths still resolve: `../../data/` for data and
`../scripts/` for the shared figure scripts.
