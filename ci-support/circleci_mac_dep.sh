#!/usr/bin/env bash
ls
pwd
export PATH=${HOME}/miniconda/bin:${PATH}
conda create -q -n py3 -c cdat/label/nightly -c nesii/label/dev-esmf -c conda-forge -c uvcdat cdms2 nose flake8 mesalib image-compare matplotlib numpy=1.13 vcs "python>3"
conda create -q -n py2 -c cdat/label/nightly -c nesii/label/dev-esmf -c conda-forge -c uvcdat cdms2 nose flake8 mesalib image-compare matplotlib numpy=1.13 vcs "python<3"
export UVCDAT_ANONYMOUS_LOG=False
source activate py2
python setup.py install
source activate py3
rm -rf build
python setup.py install
