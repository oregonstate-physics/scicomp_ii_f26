# HW 3

The purpose of this assignment is to get exercise on some basic sampling skills, focusing on rejection and importance sampling.

Take the following probability density function:
```math
p(x) = 0.164\exp{\left(-\frac{(x-10)^4}{2\cdot 8^2}\right)}
```

1. Use _rejection sampling_ to draw 1000 samples from this distribution.  Show that the samples you've drawn are correctly distributed according to this probability density function.

2. Use _importance sampling_ to estimate the expectation value of $x$, and compare it to the mean of the samples you drew in part 1.

3. Calculate the expectation value of $x^2$.

Use the **self-normalised** importance sampling estimator from the Intro to Sampling
notebook — the ratio of the two sums, $\sum_s h(x_s) w_s / \sum_s w_s$ — rather than
averaging $h(x)w(x)$ directly.  Both are valid here, but the self-normalised form is
the one the course uses, and it is far less noisy when the proposal is a poor match.

## Recording your answers

Next to your notebook there is a `submit.py`.  Use it to record each number you are
asked for:

```python
import submit

submit.answer("n_samples",      len(samples))
submit.answer("mean_rejection", samples.mean())
submit.answer("var_rejection",  samples.var())   # part 1: does the spread match p(x)?
submit.answer("E_x",            e_x)             # part 2, importance sampling
submit.answer("E_x2",           e_x2)            # part 3, importance sampling
```

That writes `answers.json`.  **Commit it along with your notebook** — a checker reads
it on every push and tells you whether each number came out in a plausible range.

You can run the same checks yourself at any time:

```
python3 tests/test_answers.py
```

These are sampled quantities, so nobody's numbers match exactly and none are expected
to.  The ranges are wide enough that any correct method passes.  If something is
flagged, the usual causes are recording a different quantity from the one asked for,
or using fewer samples than the problem specifies.

Passing the checker is a small part of the grade and is not evidence on its own — the
reasoning in your notebook and write-up is what is being assessed.

## Graduate Students

4. Revisit the importance sampling example from the Intro to Sampling notebook from class.  There we demonstrated the use of importance sampling to estimate the expectation value of some function of our random variable.  We could also use the weights we computed to probabilistically choose samples from the sampling distribution to keep, in an effort to "reweigh" the sampling distribution to correspond to the target distribution.  Try to implement this, and see if your resampled distribution's histogram matches the target distribution's probability density function.
