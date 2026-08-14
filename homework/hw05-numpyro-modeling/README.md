# Modeling w/ NumPyro

1. Use `NumPyro` to define a model containing a single random variable that follows a [Gamma](https://en.wikipedia.org/wiki/Gamma_distribution) [distribution](https://num.pyro.ai/en/stable/distributions.html#gamma) with shape parameters $\alpha=5$, $\beta=0.1$.  Here $\beta$ is the **rate**, which is what `NumPyro` expects — watch out, because `scipy.stats.gamma` instead takes a **scale**, and scale $=1/\text{rate}$. Mixing the two up is the most common mistake in this problem, and it changes the mean by a factor of 100. First draw **at least 1000 samples** directly from the distribution (10,000 is better and costs nothing) and plot the histogram and/or KDE.

2. Using the samples you've drawn, compute the mean and variance of the random variable. Modify the shape parameters individually to see how each of them affect the mean and variance of the distribution. **Report the values from the original $\alpha=5$, $\beta=0.1$ distribution**, not from the modified ones.

3. The Gamma distribution doesn't have support for negative values, making it a useful prior distribution for parameters that must be positive. Use `NumPyro` to conduct an MCMC sampling of our linear regression model with outliers from class, but replace the half-normal priors for standard deviation parameters with sensible gamma distributions (i.e., not dramatically different in scale from the half-normal distributions previously used). Does the change in prior distribution meaningfully change the posterior distributions?

## Recording your answers

Use the `submit.py` in this folder to record the three numbers from parts 1 and 2:

```python
import submit

submit.answer("n_samples",  samples.size)
submit.answer("gamma_mean", samples.mean())
submit.answer("gamma_var",  samples.var())
```

That writes `answers.json`. **Commit it along with your notebook.** You can run the
checks yourself at any time:

```
python3 tests/test_answers.py
```

`gamma_mean` and `gamma_var` must come **from the samples you drew**, not from the
formulas $\alpha/\beta$ and $\alpha/\beta^2$. Reporting the formula values will pass the
checker — nothing can tell the difference from a number alone — and will be obvious in
your notebook, where the sampling code and histogram either exist or they do not.

Part 3 and the 564 section are not auto-checked. They ask whether something changed and
why, and that is a judgement you have to argue for.

### About the sample size

The checker requires at least 1000 samples. This is not busywork: the variance of a
Gamma is a noisy thing to estimate, and at 1000 samples its sampling spread is already
±29% of the true value. At 100 samples no honest range would be narrow enough to mean
anything. Drawing 10,000 costs nothing and tightens it considerably — a good habit to
notice now, because the same argument returns for MCMC, where the number of samples you
have and the number you *effectively* have are not the same thing.

## Graduate Students
Repeat the Gaia linear regression analysis from the 564 portion of last week's homework, this time using `NumPyro`.

1. How do your results compare?
2. How about the efficiency of sampling?
3. Use the posterior predictive framework in `NumPyro` to simulate a new Gaia catalog from your model and posterior estimate.  How does it compare to the observed data?  How might we improve our model?
