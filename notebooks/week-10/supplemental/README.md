# Week 10 — supplemental

Not taught, not graded, and not required. The weekly completion check ignores this
folder; read it if the week interested you.

## `notch-filters-ligo.ipynb`

Notch filtering applied to real LIGO interferometer data, building from Gaussian noise up
to the strain around GW150914. The longest notebook in the course, and the natural next
step after `02-filters-welch-pulsars`.

It downloads the strain data at runtime from the Gravitational Wave Open Science Center,
so it needs a network connection.

## `gw-posterior-pdf.ipynb`

Inferring a black hole binary's properties from a gravitational-wave observation by
evaluating a posterior on a grid — a callback to the Bayesian weeks, and the capstone to
the LIGO notebook above.

It needs two packages that are **not** in `requirements.txt`: `pycbc` and `healpy`.
Install them yourself if you want to run it.
