# Globular Cluster Membership — NGC 6397

> **Archived project — not currently on the schedule.**
> Combines the former HW7 (M4 isochrones) with the former final project (NGC 6397
> classification). Available as a ready-made alternative for graduate students choosing
> their own project, or to return to the schedule later.

NGC 6397 is the second closest globular cluster to Earth (after M4). Using a catalog of
confidently identified members, the project trains a classifier to recognise cluster
membership from Gaia observations — then checks the candidates it finds against an
isochrone, a prediction from stellar evolution that the model never saw.

Work through `notebooks/cluster-membership.ipynb`.

## Structure

**Part 0 — Isochrones, using M4.** A guided warm-up on a cluster whose membership is
already known: read a MIST isochrone, filter by evolutionary phase, apply the distance
modulus, and overplot Gaia observations of M4. Ends by estimating the cluster's age from
the fits.

*Background reading:* [OpenStax Astronomy 2e](https://openstax.org/details/books/astronomy-2e)
§22.3 introduces stellar clusters and how they appear on the H-R diagram. §18.4 fills in
gaps on H-R diagrams generally.

**Part 1 — Classification.** Cross-match the confident members against the wider Gaia
sample, explore which observed quantities separate members from background, build and
train a model, evaluate it, and look for candidates the catalog missed.

**Part 2 — Isochrone validation.** Apply Part 0's technique to NGC 6397 and use it to argue
whether the new candidates are viable. Then retrain including colour and brightness.

**Graduate extension** at the end of the notebook.

## Data

In this project's `data/`:
- `NGC6397-1.dat` — cluster member catalog
- `gaia-NGC6397-neighborhood.csv.gz` — Gaia sources around the cluster
- `NGC6397_iso.csv` — MIST isochrone for NGC 6397
- `m4_isochrones.iso.cmd` — MIST isochrones for M4 (Part 0)

From the repository's top-level `data/` (shared with the week-08 notebook):
- `NGC6121-1.dat` — M4 member catalog
- `m4_gaia_source.csv.gz` — Gaia sources around M4

## Catalog Data
The catalog, originally pulled from [here](http://cdsarc.u-strasbg.fr/ftp/J/A+A/616/A12/), can be found in `data/NGC6397-1.dat`.

From the Gaia archive consider all objects in a 2 deg x 1.5 deg box centered on the cluster.  The query below was used to generate `data/gaia-NGC6397-neighborhood.csv.gz`.

```sql
SELECT TOP 500000 gaia_source.source_id,gaia_source.ra,gaia_source.dec,gaia_source.parallax,gaia_source.parallax_error,gaia_source.pm,gaia_source.pmra,gaia_source.pmra_error,gaia_source.pmdec,gaia_source.pmdec_error,gaia_source.phot_g_mean_mag,gaia_source.phot_bp_mean_mag,gaia_source.phot_rp_mean_mag,gaia_source.bp_rp,gaia_source.radial_velocity,gaia_source.radial_velocity_error
FROM gaiadr3.gaia_source 
WHERE 
CONTAINS(
	POINT('ICRS',gaiadr3.gaia_source.ra,gaiadr3.gaia_source.dec),
	BOX('ICRS',265.17,-53.68,2,1.5)
)=1
```

## Isochrones

The [MIST isochrone interpolator](http://waps.cfa.harvard.edu/MIST/interp_isos.html) was used to produce an isochrone based on known properties of NGC 6397 (metalicity, reddening due to dust, etc.), and saved `BP-RP`, `Gaia_G_EDR3=phot_g_mean_mag` (with distance modulus already applied), and phase (indicating stellar evolutionary phase) to `data/NGC6397_iso.csv`.