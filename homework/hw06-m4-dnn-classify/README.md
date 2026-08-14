# Identifying M4 cluster members w/ Dense Neural Networks

## Data

Everything you need is in the `data/` directory of this repo:

- `m4_gaia_source.csv.gz` — the Gaia catalogue of the field containing M4 (~495,000 stars)
- `NGC6121-1.dat` — the list of known M4 members, used to build your labels

These are the same files used in `notebooks/week-08/05-dense-nn-m4.ipynb`, so the loading
code there will work here.

## The task

Demonstrate the use of a densely connected neural network, like the one we trained on the
MNIST data set, for classifying stars in the M4 cluster using Gaia's measurements of stars'
locations on the sky (right ascension and declination). This is basically a repeat of what
we covered in class, but this time I want you to even out the training set to include
roughly equal numbers of M4 members and non-members.

1. What training and validation accuracies are you able to achieve?

2. **Now compute the accuracy of a model that labels every single star a non-member.**
   Compare it with what you got in question 1. If your trained network does not obviously
   win, that is not a bug — work out why it happens, and decide what you should be
   measuring instead. Two things to think about: what fraction of this field is actually
   in M4, and what evening out the training set does to where your model places its
   decision boundary. Whatever you decide to measure, report it and say why it is a
   fairer description of how good the model is.

3. Is your trained model confident that any of the stars in your test set are part of M4?

4. What did your model learn? Can you come up with a useful way to probe your model and
   visualize the results to answer this question?

5. Do you think more sophisticated models could do better with this classification task
   using only sky positions? Use the properties of the training set to make your argument.

## What is being graded

This one is read. There is no `answers.json` and nothing here is auto-checked beyond
whether the notebook is committed and ran without errors — questions 2, 4 and 5 are
arguments, not numbers, and the marks are in how you make them.

## Graduate Students

Make use of other features observed by Gaia to improve your classifier. Be sure to use the
data model documentation to understand what each feature is, and explain why you think it
would be useful for identifying cluster members. What accuracies can you achieve — measured
the way you argued for in question 2? Does your trained model find any stars it believes
are confidently in M4 that weren't in the M4 catalog?
