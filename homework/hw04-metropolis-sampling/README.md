# Week 4     HW

The purpose of this assignment is to use the Metropolis algorithm to infer model parameters by sampling a _posterior distribution_.  Let's return to our linear regression problem.

Using the synthetic $x-y$ data set from [Hogg, Bovy, and Lang (2010)](https://arxiv.org/abs/1008.4686) (in the `data` directory of this repo), assume a **uniform prior** over slope and y-intercept and use the Metropolis algorithm to draw samples from the posterior density function describing our knowledge of the slope and y-intercept given the observed data.

To do this you will have to extend our 1-D Markov chains from class to 2-D, meaning we have a 2-D parameter space to explore and you will have to decide a method (or methods) to propose moves in those two dimensions.

**Use all 20 data points.** Four of them are visibly off the trend — that is deliberate on Hogg's part, and the temptation to drop them is the right instinct at the wrong time. Week 5 comes back to this data and models the outliers properly instead of discarding them. Cutting them here changes the slope by fifteen standard deviations, so it is not a small decision made quietly.

Show the quality of the fit to the data and the associated uncertainty by plotting the lines corresponding to several samples from your chain on top of the data

Make one or several figures showing your estimate of the 2-D posterior distribution.  Are there correlations between the model parameters?

## Recording your answers

Use the `submit.py` in this folder to record six numbers from your chain, after
discarding burn-in:

```python
import submit

submit.answer("n_eff",   effective_sample_size)   # see below
submit.answer("m_mean",  chain_m.mean())
submit.answer("b_mean",  chain_b.mean())
submit.answer("m_sd",    chain_m.std(ddof=1))     # the WIDTH of the posterior
submit.answer("b_sd",    chain_b.std(ddof=1))
submit.answer("corr_mb", np.corrcoef(chain_m, chain_b)[0, 1])
```

That writes `answers.json`. **Commit it along with your notebook.** Check yourself at
any time with `python3 tests/test_answers.py`.

`m_sd` and `b_sd` are the standard deviations **of the posterior samples** — how wide
your knowledge of each parameter is. They are not the uncertainty on the mean, which is
smaller by roughly $\sqrt{N}$ and is not what is being asked for.

### Your chain has to have actually mixed

You are also asked for `n_eff`, the **effective sample size** — the number of
*independent* samples your chain is worth. Successive Metropolis steps are correlated,
so a chain of 20,000 steps is never worth 20,000 draws, and how much less depends
entirely on your proposal. Estimate it from the autocorrelation, as in
`notebooks/week-03/01-intro-to-sampling.ipynb`:

$$N_\text{eff} = \frac{N}{\tau}$$

**The checker requires $N_\text{eff} \ge 100$.** This is the one requirement here that
is really about method rather than arithmetic, and it is not a formality — with a poorly
mixing chain your posterior mean is simply not determined well enough to check, and no
honest tolerance would be narrow enough to mean anything.

If you cannot reach 100, the problem is almost certainly your proposal distribution, and
the reason is the question the assignment already asked you: *are there correlations
between the model parameters?* Answer that one first and look at what it implies about
which directions in $(m, b)$ your proposal should be willing to move in, and how far.
A single step size used for both parameters will not get you there at any value.

The graduate section is not auto-checked — it involves a cut made by eye, so there is no
single right answer to compare against.

## Graduate Students

Use the same technique for constraining a linear model connecting the color and brightness of nearby main sequence stars observed by Gaia (parallax > 40 mas).  To do this you will need to:

1. Select only the stars from the data set with parallax > 40 mas.
2. (crudely) remove the white dwarfs (constructing a dividing line by eye is fine for this).
3. Define your likelihood.  This will be similar to the last linear regression likelihood, except that we don't have uncertainties on measurements of the brightness, Mg.  Even if we did, the scatter about the linear relationship is due to physics not measurement uncertainty, so we'll need to infer it from the data.
4. Define priors.  Uniform priors on slope and y-intercept are fine, but you'll need to impose a prior on the scatter in $M_G$ about the line, $\sigma_{M_G}$, that ensures it stays positive and doesn't run away.  I suggest a normal distribution with $\sigma \sim 5$ for $\sigma_{M_G} > 0$.
5. Perform your first 3-D MCMC.

Show the quality of the fit to the data and the associated uncertainty by plotting the lines corresponding to several samples from your chain on top of the data.

Are there correlations between the constraints on the model parameters?

What did we infer regarding the scatter about the line, $\sigma_{M_G}$, and how does it compare to your by-eye assessment of the width of the scatter along the main sequence?
