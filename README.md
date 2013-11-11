2014-kbase-dev
==============

Objective:

Given a metadata measurement, e.g., pH, identify functions with a significant correlation.  I used linear regression.
Note that this isn't useful unless you have an appropriate number of samples.  In this example, three samples is
just for demonstration.

To download abundance data and metadata, see:
get-functions.sh

To run:
python lr.py ph abundance.txt mgm*

