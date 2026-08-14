# Extra projects — not currently on the schedule

Complete assignments that are not part of the current term's sequence. They live here
rather than in `homework/` so the numbered assignments stay an honest record of what is
actually assigned.

These are not abandoned. Uses:

- **A ready-made alternative for graduate students.** Graduate students design their own
  final project, but not everyone arrives with a dataset and a question. Anything here is a
  complete, tested option to take instead.
- **Returning content to the schedule.** Each folder is self-contained — README, notebook,
  and its own data.
- **Reference** for how a project of this scope is structured.

## `ngc6397-cluster-membership/`

Globular cluster membership in NGC 6397, with a guided M4 isochrone warm-up. Merges what
were formerly HW7 (M4 isochrones) and the final project (NGC 6397 classification) — the
first teaches the technique, the second applies it, and they read better together than
apart.

Train a classifier to identify cluster members from Gaia astrometry and photometry, then
validate the candidates it finds against an isochrone — a prediction from stellar evolution
that the model never saw. That last move, *checking a machine-learning result against
independent physical theory*, is the point of the project.

Needs `NGC6121-1.dat` and `m4_gaia_source.csv.gz` from the repository's top-level `data/`,
which the week-08 notebook also uses.

## Restoring one

Move the folder into `homework/`, number it into the sequence, add it to the homework table
in the top-level `README.md`, and check its relative paths still resolve — data one
directory up from `notebooks/`, and `../../../../data/` for anything shared.
