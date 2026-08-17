# HW 1 — Probability

The assignment itself is in [`probability.ipynb`](probability.ipynb):
three problems on conditional probability, transforming distributions, and the Gaussian.

## Recording your answers

Alongside the notebook there is a `submit.py`.  Use it to record each number the
assignment asks for:

```python
import submit

# Problem 1 -- your answers to parts 2 and 3
submit.answer("p1_2", ...)               # P(two females | at least one female)
submit.answer("p1_3", ...)               # P(two females | older is female)

# Problem 2
submit.answer("mean_x",   x.mean())
submit.answer("mean_y",   y.mean())
submit.answer("median_x", np.median(x))
submit.answer("median_y", np.median(y))
submit.answer("pdf_y_at_0p5", pdf_y(0.5))   # your part-4 pdf, evaluated at y = 0.5

# Problem 3
submit.answer("frac_above_145", ...)        # part 3
submit.answer("iq_one_in_million", ...)     # part 4
```

That writes `answers.json`.  **Commit it along with your notebook** — a checker reads it
on every push and tells you whether each number came out in a plausible range.

You can run the same checks yourself at any time:

```
python3 tests/test_answers.py
```

Record the value you computed, not a rounded version of it.

### What is being checked

Most of HW1's answers are **exact** — the conditional probabilities, the transformed
pdf, and both Gaussian results have one right value, so those checks are tight.  The
four sample statistics vary from run to run and are checked against a range wide enough
that any correct method passes.

One check compares two of your own answers to each other: `median_y` against
`log10(median_x)`.  Problem 2 part 5 makes the point that a monotonic transform leaves
the median alone, and that check is just that statement.  It holds for any correct
sample, so nothing about it depends on luck.

Passing the checker is a small part of the grade and is not evidence on its own — the
reasoning in your notebook and write-up is what is being assessed.  Problem 1 in
particular is graded on the derivation; getting the number right without the tree
diagram earns very little.

## Graduate Students

Problem 3 gave you $\mu$ and $\sigma$ and asked for a tail fraction, so the answer was
exact. Real data does not arrive that way. `data/iq_sample.csv` holds **500 scores
collected at one testing site** — a population of its own, not the textbook calibration.

1. Estimate $\mu$ and $\sigma$ from the sample.
2. Using your estimates, compute $P(\text{IQ} > 145)$ for this population. Compare it with
   the answer you got in Problem 3 for the standard $N(100, 15)$.
3. **Put an uncertainty on it.** Your $\hat\mu$ and $\hat\sigma$ are themselves estimates
   with sampling error, and the tail fraction inherits it. Propagate that through and
   report $\sigma_p$.

   There is more than one defensible way — analytic propagation, or resampling. Say which
   you used and why.

4. Which of $\hat\mu$ and $\hat\sigma$ does the answer depend on more? Justify it, and say
   what that implies about estimating a far tail from a finite sample. Your uncertainty in
   part 3 should be a large fraction of $p$ itself; that is not a mistake, it is the point.

Record these alongside the others:

```python
submit.answer("mu_hat", ...)
submit.answer("sigma_hat", ...)
submit.answer("p_hat", ...)
submit.answer("p_uncertainty", ...)
```

You will be graded on the reasoning in part 4 as much as on the numbers. Note that
`n = 500` gives you roughly **one** person above 145 — so this is a genuine extrapolation
into a tail the data barely samples, which is exactly why the uncertainty is large.
