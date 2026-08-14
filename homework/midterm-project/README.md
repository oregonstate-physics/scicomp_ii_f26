# Midterm Project

For this project we will use the [Gaia DR3 data release](https://gea.esac.esa.int/archive/) to explore the solar neighborhood. This is the same selection of data we've explored recently, which can be pulled from the Gaia data archive with the following query:

```sql
SELECT TOP 300000 phot_g_mean_mag+5*log10(parallax)-10 AS mg, bp_rp, parallax FROM gaiadr3.gaia_source
WHERE parallax_over_error > 10
AND parallax > 10
AND phot_g_mean_flux_over_error>50
AND phot_rp_mean_flux_over_error>20
AND phot_bp_mean_flux_over_error>20
AND phot_bp_rp_excess_factor < 1.3+0.06*power(phot_bp_mean_mag-phot_rp_mean_mag,2)
AND phot_bp_rp_excess_factor > 1.0+0.015*power(phot_bp_mean_mag-phot_rp_mean_mag,2)
AND visibility_periods_used>8
AND astrometric_chi2_al/(astrometric_n_good_obs_al-5)<1.44*greatest(1,exp(-0.4*(phot_g_mean_mag-19.5)))
```

The data is also in the `data/` directory of this repository.

Using a subset of this data, we're going to focus on constructing models and inferring the parameters of those models using `NumPyro`.

## Data Down-Selection

To avoid lengthy run times we'll focus on only the nearby data.  Select out the objects with parallax > 40 milliarcseconds.


# Part I

For this part we'll remove (crudely) the white dwarf population (the dim secondary population of stars).  To do this we'll use a simple linear boundary to divide the population:

```python
x1, y1 = 0, 8
x2, y2 = 3, 16.5
m_div = (y2 - y1)/(x2 - x1)
b_div = y1 - m_div * x1
```

where we'll be focusing on the objects with $M_G < m_\mathrm{div} (BP-RP) + b_\mathrm{div}$.

1. Construct a `NumPyro` model that models the population as a line, assuming $M_G$ to be distributed normally about this line with a standard deviation to be inferred from the data.  Perform an MCMC.

    A. Discuss the differences between the prior distributions you choose for your model parameters and the marginal (i.e., one-dimensional) posterior distributions estimated with your MCMC.  Did you choose suitably uninformed priors?

    B. Plot the models corresponding to 50 randomly chosen posterior samples from your MCMC.  Discuss the quality of the fit, and in particular the role that the standard deviation parameter is playing in this fit.

2. Construct a new model that models the relation between $(BP-RP)$ and $M_G$ quadratically.  Carefully choose priors; be sure to explore choices for locations and scales that are appropriate for the new parameters.  Run an MCMC.

    A. Discuss the differences between the prior distributions you choose for your model parameters and the marginal (i.e., one-dimensional) posterior distributions estimated with your MCMC.  Did you choose suitably uninformed priors?

    B. Plot the model corresponding to 50 randomly chosen posterior samples from your MCMC.  Discuss the quality of the fit.

    C. **Graduate Students:** Use your posterior estimates to predict the distribution we would expect for $M_G$ values of main sequence stars with color $(BP-RP) = 6$.

3. **Graduate Students:** Explore higher order polynomials a bit.  How does the (qualitative) quality of the fit behave?

# Part II

Now let's bring the white dwarfs back into the mix, focusing on all the objects with parallax > 40 milliarcseconds.

1. Construct a mixture model with `NumPyro` that simultaneously describes the main sequence stars and white dwarfs, each described by a linear relationship with its own slope, y-intercept, and scatter of observations about it.

    **Tips:**
    1. Recall our outlier model we built, which outlines the machinery for building a mixture model that allows for our data to be described by more than one distribution.
    1. Our model will now be composed of two lines.  If we impose the same priors for the parameters of each line, then the two lines will be degenerate and sampling gets unnecessarily tricky.  There are many ways we could avoid this degeneracy, but for now I suggest imposing unique priors on the y-intercepts.  I also recommend a relatively narrow prior on the slopes of the lines to get the model from trying crazy solutions:
        ```python
        m_ms = numpyro.sample('m_ms', dist.Uniform(2, 5))
        b_ms = numpyro.sample('b_ms', dist.Uniform(0, 5))

        m_wd = numpyro.sample('m_wd', dist.Uniform(2, 5))
        b_wd = numpyro.sample('b_wd', dist.Uniform(10, 15))
        ```
2. Plot the two lines for each of 50 randomly chosen posterior samples from your MCMC.  Discuss the quality of the fits, and in particular the constraints.  Is the model able to identify the two populations?

3. **Graduate Students:**
    A. Plot a distribution of the probabilities that each star in our catalog is on the main sequence.  Are there any stars which aren't confidently associated with a particular population?
    B. Relax the priors on slope and y-intercept and run an MCMC:
    ```python
    m_ms = numpyro.sample('m_ms', dist.Normal(scale=10))
    b_ms = numpyro.sample('b_ms', dist.Normal(scale=20))

    m_wd = numpyro.sample('m_wd', dist.Normal(scale=10))
    b_wd = numpyro.sample('b_wd', dist.Normal(scale=20))
    ```
    Take a look at the trace plots and the fits to the data.  Can you describe what's happening?

## Graduate Students

The graduate items are placed inside the parts they extend rather than collected here,
because each one builds directly on the model in that part. They are:

- **Part I, 2.C** — predict the distribution of $M_G$ for main sequence stars at
  $(BP-RP) = 6$, using your quadratic posterior. Note this colour lies beyond the reddest
  star in the selection, so you are extrapolating; say what that does to your answer.
- **Part I, 3** — explore higher order polynomials, and describe how the quality of the
  fit behaves.
- **Part II, 3** — see that part for the mixture-model extension.
