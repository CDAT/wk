#!/usr/bin/env bash
ls
pwd
export PATH=${HOME}/miniconda/bin:${PATH}
conda create -q -n py3 -c uvcdat/label/nightly -c nadeau1  -c conda-forge -c uvcdat "cdms2>2.12.2017" nose flake8 "python>3" mesalib image-compare "matplotlib<2.1" numpy=1.13 "vcs>2.12.2017"
conda create -q -n py2 -c uvcdat/label/nightly -c conda-forge -c uvcdat "cdms2>2.12.2017" nose flake8 mesalib image-compare "matplotlib<2.1" numpy=1.13 "vcs>2.12.2017"
export UVCDAT_ANONYMOUS_LOG=False
source activate py2
python setup.py install
source activate py3
rm -rf build
python setup.py install
