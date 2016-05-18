#!/bin/sh

# file: mergeForceCoefficientsFigures.sh
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Merges the two .pdf into a single .pdf page.


INFILE1="openfoam_forceCoefficientsRe2000AoA30.pdf"
INFILE2="openfoam_forceCoefficientsRe2000AoA35.pdf"
OUTFILE="openfoam_forceCoefficientsRe2000.pdf"

pdfjam $INFILE1 $INFILE2 --nup 1x2 --outfile $OUTFILE

rm -f $INFILE1 $INFILE2

