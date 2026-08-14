# Scientific Computing II — PH 464/564

Course source for **PHYS 464/564: Physical Data Analysis (Scientific Computing II)**,
OSU Physics.

Much of this material derives from notebooks and activities developed by **Ben Farr**
for his scientific computing class at the University of Oregon and by **Stephen Taylor**
for his astrostatistics class at Vanderbilt.

> **This is the perennial source repo.** It is year-agnostic and keeps notebook outputs.
> The public per-term student copy is *generated* from it — see `tools/make_student_copy.py`.
> Never edit the student copy directly.

New here? Start with [docs/getting-started.md](docs/getting-started.md).

## Layout

| Path | What |
|---|---|
| `notebooks/` | lecture notebooks, one folder per teaching week |
| `homework/` | one self-contained folder per assignment, numbered to match Canvas |
| `data/` | shared datasets (provenance documented below) |
| `docs/` | orientation material |
| `tools/` | instructor tooling — excluded from the student copy |

Week folders mirror the Canvas modules, so `week-04/` holds exactly what is taught in
week 4. The folder *names* never change between offerings — only their contents move
when the schedule shifts.

`notebooks/scripts/` holds figure scripts shared by notebooks in different weeks;
`notebooks/extras/` holds notebooks not currently on the schedule.

## Notebooks

One folder per teaching week, matching the Canvas modules. Week 0 has no lecture
notebooks — see [docs/getting-started.md](docs/getting-started.md) and
[hw00](homework/hw00-getting-started).

### Week 1 — Probability
* [Motivation](notebooks/week-01/01-motivation.ipynb) — why statistical reasoning matters in physics
* [Probability intro](notebooks/week-01/02-probability-intro.ipynb) — probability, conditionals, transforming distributions
* [Descriptive statistics & PDFs](notebooks/week-01/03-descriptive-stats-pdfs.ipynb) — summary statistics and common distributions

### Week 2 — Data exploration, multivariate distributions
* [Birth data exploration](notebooks/week-02/01-birth-data-exploration.ipynb) — US birth rates; getting comfortable with pandas and matplotlib
* [Multivariate distributions & the CLT](notebooks/week-02/02-multivariate-clt.ipynb) — covariance, the central limit theorem, first sampling

### Week 3 — Sampling and regression
* [Intro to sampling](notebooks/week-03/01-intro-to-sampling.ipynb) — rejection and importance sampling
* [Intro to regression](notebooks/week-03/02-intro-to-regression.ipynb) — linear regression in a generative framing

### Week 4 — Gaia, frequentist and Bayesian analysis
* [Solar neighborhood with Gaia](notebooks/week-04/01-solar-neighborhood-gaia.ipynb) — Gaia data and an observational H-R diagram
* [Maximum likelihood](notebooks/week-04/02-maximum-likelihood.ipynb) — frequentist parameter estimation
* [Bayes](notebooks/week-04/03-bayes.ipynb) — priors, posteriors, and Bayesian inference
* [battleship-priors.pdf](notebooks/week-04/battleship-priors.pdf) — in-class activity on priors

### Week 5 — NumPyro
* [Intro to NumPyro](notebooks/week-05/01-intro-to-numpyro.ipynb) — JAX and NumPyro for probabilistic modeling and efficient MCMC
* [Modeling outliers](notebooks/week-05/02-modeling-outliers.ipynb) — a mixture model for outliers in linear regression

### Week 6 — Model building, intro to ML
* [CO2 at Mauna Loa](notebooks/week-06/01-co2-mauna-loa.ipynb) — progressively richer models of atmospheric CO2
* [Intro to machine learning](notebooks/week-06/02-intro-to-ml-gaia.ipynb) — ML concepts and vocabulary, rephrasing regression

### Week 7 — Logistic regression, and superconductivity
* [Logistic regression](notebooks/week-07/01-logistic-regression.ipynb) — binary classification, built from scratch on 2-D synthetic data
* [Superconductivity](notebooks/week-07/02-superconductivity.ipynb) — what Tc is and why predicting it is an open problem; 81 real features, chemical families, and classifying about the 40 K BCS ceiling. Introduces the dataset used by the final project.

### Week 8 — Multiclass classification and neural networks
* [Multiclass classification](notebooks/week-08/01-multiclass-classification.ipynb) — one-vs-all beyond two classes
* [Intro to neural networks](notebooks/week-08/02-intro-to-neural-networks.ipynb)
* [Intro to Flax](notebooks/week-08/03-intro-to-flax.ipynb) — a dense layer used for linear regression
* [Dense NN on MNIST](notebooks/week-08/04-dense-nn-mnist.ipynb) — classifying handwritten digits
* [Dense NN on M4](notebooks/week-08/05-dense-nn-m4.ipynb) — identifying cluster members from Gaia observations

### Week 9 — Convolutional neural networks, and into signal processing
* [Intro to CNNs](notebooks/week-09/01-intro-to-cnns.ipynb)
* [Volcanoes on Venus](notebooks/week-09/02-venus-volcanoes.ipynb) — classifying Magellan radar images
* [Intro to signal processing](notebooks/week-09/03-intro-to-signal-processing.ipynb) — time series and the discrete Fourier transform, derived from scratch

### Week 10 — Time series and signal processing
* [Frequency resolution & windowing](notebooks/week-10/01-frequency-resolution-windowing.ipynb) — resolution, windowing, spectrograms
* [Filters, Welch method, pulsars](notebooks/week-10/02-filters-welch-pulsars.ipynb)
* [Notch filters & LIGO data](notebooks/week-10/03-notch-filters-ligo.ipynb) — Gaussian noise and real interferometer data

### Not currently scheduled
See [notebooks/extras/](notebooks/extras) — the Boltzmann/Ising notebook and a
gravitational-wave posterior notebook, both written but not taught in the most
recent offering.

## Homework

Numbered to match Canvas. Each folder is self-contained.

| # | Folder | Topic |
|---|---|---|
| HW0 | [hw00-getting-started](homework/hw00-getting-started) | git, GitHub, and the coding environment |
| HW1 | [hw01-probability](homework/hw01-probability) | conditional probability, transforming distributions, Gaussians |
| HW2 | [hw02-birth-and-movie](homework/hw02-birth-and-movie) | data exploration with US births and TMDB |
| HW3 | [hw03-intro-sampling](homework/hw03-intro-sampling) | rejection and importance sampling |
| HW4 | [hw04-metropolis-sampling](homework/hw04-metropolis-sampling) | Metropolis MCMC for linear regression |
| HW5 | [hw05-numpyro-modeling](homework/hw05-numpyro-modeling) | probabilistic modeling with NumPyro |
| HW6 | [hw06-m4-dnn-classify](homework/hw06-m4-dnn-classify) | dense neural network classifier for M4 |
| HW7 | [hw07-llm-signal-processing](homework/hw07-llm-signal-processing) | LLM-assisted signal processing: find an unidentified signal in radio data |
| — | [midterm-project](homework/midterm-project) | Bayesian inference on the Gaia H-R diagram |
| — | [final-project](homework/final-project) | predicting superconducting critical temperature |

Not currently assigned: see [homework/extras/](homework/extras) for the archived NGC 6397
cluster-membership project (former HW7 + former final project, merged).

## Data Provenance

**Note on file format:** the larger data files are stored gzipped (`.csv.gz`)
so this repository needs no `git-lfs`. `pandas` reads them transparently —
`pd.read_csv('../data/m4_gaia_source.csv.gz')` works exactly like the uncompressed file.
The commands and queries below reproduce the *uncompressed* originals; run `gzip` on the
result to match what is committed here.

### Exploring births in the US

US Birth data from the Social Security Administration, prepared by FiveThirtyEight.

[source](https://github.com/fivethirtyeight/data/tree/master/births)

This data can be with a wget command:

```bash
mkdir -p ../data
wget -qO ../data/US_births_2000-2014_SSA.csv https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_2000-2014_SSA.csv
```

### Solar Neighborhood w/ Gaia

We will use the [Gaia DR3 data release](https://gea.esac.esa.int/archive/) to explore the solar neighborhood. The data is available from the Gaia Archive. We will use the following query to get the data:

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

### Synthetic data for linear regression

This data accompanies [Hogg, Bovy, and Lang (2010)](https://arxiv.org/abs/1008.4686).  It can be downloaded directly with

```bash
!wget -o ../data/data_yerr.dat https://raw.githubusercontent.com/davidwhogg/DataAnalysisRecipes/master/straightline/src/data_yerr.dat
```

### CO<sub>2</sub> Concentrations in Mauna Loa, Hawaii

Monthy-averaged CO<sub>2</sub> concentrations measured in Mauna Loa, Hawaii, hosted by the NOAA:

```bash
!wget -q ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt -O ../data/co2_mm_mlo.txt
```

### Logistic Regression Synthetic Data

To introduce logistic regression we make use of some data used by Jordi Warmenhoven in their [Coursera Machine Learning course](https://github.com/JWarmenhoven/Coursera-Machine-Learning). 
```bash
!wget https://raw.githubusercontent.com/JWarmenhoven/Coursera-Machine-Learning/master/notebooks/data/ex2data1.txt -O ../data/ex2data1.txt
!wget https://raw.githubusercontent.com/JWarmenhoven/Coursera-Machine-Learning/master/notebooks/data/ex2data2.txt -O ../data/ex2data2.txt
```

### SDSS Quasars

This is data collected by the Sloan Digital Sky Survey (SDSS) relating to quasars. The catalogs we'll be using are part of [PSU's astrostatistics data sets](https://astrostatistics.psu.edu/datasets/index.html).  We need three separate files, separated by spectroscopically confirmed classifications.

Spectroscopically confirmed stars:
```bash
!wget -q --no-check-certificate -O ../data/SDSS_stars.csv https://astrostatistics.psu.edu/MSMA/datasets/SDSS_stars.csv
```

white dwarfs:
```bash
!wget -q --no-check-certificate -O ../data/SDSS_wd.csv https://astrostatistics.psu.edu/MSMA/datasets/SDSS_wd.csv
```

and quasars:
```bash
!wget -q --no-check-certificate -O ../data/SDSS_quasar.dat https://astrostatistics.psu.edu/datasets/SDSS_quasar.dat
```

More info on the dataset can be found [here](https://astrostatistics.psu.edu/datasets/SDSS_quasar.html).

### Volcanoes on Venus

110×110 pixel radar "chips" of the Venusian surface from the
[Magellan mission](https://www2.jpl.nasa.gov/magellan/), processed by Manuel Mena and hosted
on Kaggle: https://www.kaggle.com/datasets/fmena14/volcanoesvenus

**Downloading from Kaggle requires a free account** — students do not need one, since a
prepared copy ships in `data/venus/`.

Kaggle distributes the chips as CSV (12,100 text columns per image): 283 MB for training,
110 MB for test, both over GitHub's 100 MB limit, and `pandas` expands the training set to
646 MB in memory. `data/venus/` instead holds compressed `uint8` arrays — 34 MB and 25 MB,
loading in ~0.2 s. The test set is complete; the training set is a **stratified subsample of
4,001 of the original 7,000**, preserving the ~14% positive class balance and the rarer
volcano `Type` categories. Rebuild with:

```bash
python3 tools/build_venus_dataset.py
```

### `homework/hw07-llm-signal-processing/data/search_data_01.fil` — radio search-mode data

38.2 s of single-dish radio telescope data: 96 frequency channels across
1352.5–1447.5 MHz, 72 µs sampling, 4-bit, in SIGPROC filterbank format.

**Provenance is deliberately withheld here.** This is the dataset for the HW7 search
exercise, and knowing where it came from would give away what is in it. The full source,
the original filename, and the answer are documented in
`tools/anonymize_filterbank.py` (instructor-only) and are revealed after the assignment.

The header has had its pointing coordinates and original filename removed for the same
reason. Everything needed for the analysis — `nchans`, `fch1`, `foff`, `tsamp`, `nbits`,
`nifs`, `tstart` — is intact.

### Superconducting critical temperatures

21,263 superconductors with measured critical temperatures, described by 81 statistical
summaries of elemental properties computed from composition. From Hamidieh (2018),
*Computational Materials Science* **154**, 346–354; hosted at the
[UCI Machine Learning Repository (dataset 464)](https://archive.ics.uci.edu/dataset/464/superconductivty+data)
and derived from the [NIMS SuperCon database](http://supercon.nims.go.jp/index_en.html).

The final project uses a seeded 90/10 split of the original `train.csv` and `unique_m.csv`,
with `critical_temp` removed from the holdout portion. Rebuild it with:

```bash
pip install pandas
python3 tools/build_superconductivity_split.py
```

Note that `ucimlrepo`'s `fetch_ucirepo(id=464)` returns **only** `train.csv` — it omits
`unique_m.csv`, where the chemical formulas live — so the script pulls the zip archive
directly.

### M4

We make use of two separate data products from the Gaia collaboration. First is a cluster catalog [here](http://cdsarc.u-strasbg.fr/ftp/J/A+A/616/A12/files/NGC6121-1.dat), which is associated with [this paper](https://www.aanda.org/articles/aa/abs/2018/08/aa32698-18/aa32698-18.html) looking at the kinematics of many globular clusters.  The full data release associated with the paper can be found [here](http://cdsarc.u-strasbg.fr/viz-bin/qcat?J/A+A/616/A12), and includes tables of members identified for each cluster they studied. This can be downloaded directly with:
```bask
wget http://cdsarc.u-strasbg.fr/ftp/J/A+A/616/A12/files/NGC6121-1.dat -O ../data/NGC6121-1.dat
```

Second, we use `m4_gaia_source.csv.gz`, which was pulled from the Gaia data archive with the following query:
```sql
SELECT TOP 1000000 gaia_source.designation,gaia_source.source_id,gaia_source.ra,gaia_source.dec,gaia_source.parallax,gaia_source.parallax_error,gaia_source.parallax_over_error,gaia_source.pm,gaia_source.pmra,gaia_source.pmra_error,gaia_source.pmdec,gaia_source.pmdec_error,gaia_source.astrometric_n_good_obs_al,gaia_source.astrometric_chi2_al,gaia_source.visibility_periods_used,gaia_source.phot_g_mean_flux_over_error,gaia_source.phot_g_mean_mag,gaia_source.phot_bp_mean_flux_over_error,gaia_source.phot_bp_mean_mag,gaia_source.phot_rp_mean_flux_over_error,gaia_source.phot_rp_mean_mag,gaia_source.phot_bp_rp_excess_factor,gaia_source.bp_rp,gaia_source.radial_velocity,gaia_source.radial_velocity_error
FROM gaiadr3.gaia_source 
WHERE 
CONTAINS(
	POINT('ICRS',gaiadr3.gaia_source.ra,gaiadr3.gaia_source.dec),
	BOX('ICRS',246,-26.5,3,3)
)=1
```