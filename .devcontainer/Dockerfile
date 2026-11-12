FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Two system libraries the Python packages cannot supply themselves:
#   libhdf5-dev  -- HDF5 headers, so h5py can build against the system library
#   ffmpeg       -- pydub shells out to it to render audio (week 10)
#
# These used to come from ghcr.io/rocker-org/devcontainer-features/apt-packages.
# That feature is gone because `apt-get update` cannot succeed in this base image
# as shipped. It carries /etc/apt/sources.list.d/yarn.list pinned to
#
#     signed-by=/usr/share/keyrings/yarn-archive-keyring.gpg
#
# and that keyring holds only Yarn's original signing key (72ECF46A56B4AD39...).
# Yarn now signs its release files with 62D54FD4003F6525, which is not in the
# keyring, so apt rejects the repository as unsigned and exits 100 -- killing the
# feature before it installed anything. Nothing in this course uses Yarn, so the
# source is deleted rather than re-keyed. If a later base image drops yarn.list
# on its own, the `rm -f` is simply a no-op.
RUN rm -f /etc/apt/sources.list.d/yarn.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      libhdf5-dev \
      ffmpeg \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
