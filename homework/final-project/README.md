# Final Project — Predicting Superconducting Critical Temperature

## The physics, in brief

*Week 7 covers this properly; what follows is the minimum needed for this project to
stand on its own.*

A superconductor carries direct current with **zero resistance** below a critical
temperature **Tc**, and expels magnetic flux (the Meissner effect). Tc is a
phase-transition temperature, and it is the number that decides whether a material is
laboratory curiosity or usable technology — every application, from MRI magnets to maglev,
is gated by how much cryogenics it demands.

**BCS theory (1957)** explains conventional superconductivity as electrons bound into Cooper
pairs by lattice vibrations. Because the pairing is mediated by phonons, the mechanism has a
practical ceiling — conventionally quoted as somewhere around **30–40 K** at ambient
pressure. For thirty years that ceiling held.

**It broke in 1986**, when Bednorz and Müller found superconductivity in a copper-oxide
ceramic. The **cuprates** climbed rapidly past liquid nitrogen (77 K), and the best sit near
135 K. A second unconventional family, the **iron-based** superconductors, arrived in 2008.
Neither has a settled microscopic theory. **There is still no way to predict Tc from first
principles for these materials** — which is precisely why an empirical, data-driven approach
is not a shortcut here but the way the field actually proceeds.

**One caveat that matters for this dataset.** The highest Tc recorded in it is **185 K, for
H₂S** — a hydride, superconducting only under pressures of order a *million* atmospheres.
**The 81 features describe composition and nothing else; there is no pressure column.** So
the single most extreme point in the data was measured under conditions the features cannot
represent, sitting alongside ambient-pressure cuprates. Keep that in mind when your model
tells you something confident about hydrogen compounds.

## The data

| File | Rows | Contents |
|---|---|---|
| `data/superconductor_train.csv.gz` | 19,137 | 81 composition-derived features **+ `critical_temp`** |
| `data/superconductor_test.csv.gz` | 2,126 | the same 81 features — **no `critical_temp`** |
| `data/composition_train.csv.gz` | 19,137 | per-element amounts, the chemical formula, **+ `critical_temp`** |
| `data/composition_test.csv.gz` | 2,126 | per-element amounts and formula — **no `critical_temp`** |

The 81 features are statistical summaries (mean, weighted mean, geometric mean, entropy,
range, standard deviation) of elemental properties — atomic mass, first ionisation energy,
atomic radius, density, electron affinity, fusion heat, thermal conductivity, valence —
computed from each material's composition.

Every row has an `id`. The `train` and `composition` files share ids, so you can join them.

### The test set

**2,126 materials have had their critical temperature removed.** They have been measured —
the values exist — but you do not get to see them. You will submit predictions and they will
be scored against the real answers.

This is not an artificial exercise. It is how you find out whether a model generalises, as
opposed to whether it has memorised. A model that looks excellent on data it trained on and
falls apart on the test set has told you something important about itself.

**You will therefore need a third split of your own.** Never tune a model against the data
you use to report its performance. Hold a *validation* set out of `..._train.csv.gz` for
choosing between models and settings, and keep the provided test set for the single final
evaluation. If you select a model by its test score, the score stops meaning anything.

## What to do

### Part 1 — Regression: predict Tc

1. Load and explore the training data. Tc spans 0 to 185 K and is strongly skewed — show its
   distribution and decide whether you want to model it directly or transform it.
2. Which features look informative? Justify your choices with figures, not intuition alone.
3. Build and train a regression model. The type is up to you. **Show your process** — what
   you tried, what failed, what you changed.
4. How well does it perform, and how do you know? Be specific about how you separated model
   selection from model evaluation.
5. **Predict Tc for the test set** and save your predictions (format in the notebook).

### Part 2 — Classification: warm or cold

Conventional phonon-mediated superconductivity is generally understood to have a ceiling
somewhere around 40 K. Above that, a different mechanism is usually implicated.

1. Recast the problem as binary classification about that 40 K boundary and train a
   classifier.
2. How does its performance compare with thresholding your Part 1 regression predictions?
   Which is the better approach here, and why?
3. **Classify the test set** and save those predictions too.
4. Thresholding a continuous quantity throws information away. What did you lose, and was
   anything gained?

### Part 3 — Does the physics agree?

Your model has never seen a Hamiltonian. It knows nothing about pairing mechanisms. So its
predictions can be checked against physics it was never given.

Using `composition_train.csv.gz`, materials can be sorted into families by what they
contain — cuprates (Cu and O), iron-based (Fe with As, Se, P or S), hydrides, and everything
else.

1. Characterise the Tc distribution of each family in the training data. What do you find?
2. Now look at your **test predictions**. Which families do your highest-Tc predictions
   fall into? Is that consistent with what Part 3.1 showed?
3. Does your model predict any conventional material above the ~40 K ceiling? For each such
   case: a genuine prediction worth following up, or an artifact of your model? **Argue it
   from the composition, not from the model's confidence.**
4. Suppose your model gets a material badly wrong. Give at least two distinct explanations,
   and say how you would tell them apart.

## A note on the data

This dataset is public and widely mirrored, so the withheld values could be looked up. Doing
so would produce a perfect score and demonstrate nothing. **The test score is a small part
of the grade** — the reasoning, the figures, and your account of what the model learned are
what is being assessed, and those cannot be looked up.

## Data provenance

Hamidieh, K. (2018), *A data-driven statistical model for predicting the critical temperature
of a superconductor*, Computational Materials Science 154, 346–354.

Source: [UCI Machine Learning Repository, dataset 464](https://archive.ics.uci.edu/dataset/464/superconductivty+data),
derived in turn from the [NIMS SuperCon database](http://supercon.nims.go.jp/index_en.html).

The files here are a seeded 90/10 split of the original `train.csv` and `unique_m.csv`,
produced by `tools/build_superconductivity_split.py`.

## Graduate Students

1. Train only on cuprates, then predict on iron-based superconductors. How badly does it
   transfer, and what does that tell you about what your model learned — chemistry, or
   something narrower?
2. The 81 features are all *statistical summaries of composition*. What can a model built on
   them not, even in principle, know about a material? Relate this to why predicting Tc from
   first principles is hard.
3. Put an uncertainty on your predictions, not just a point estimate. Are your errors larger
   where you predicted they would be?
