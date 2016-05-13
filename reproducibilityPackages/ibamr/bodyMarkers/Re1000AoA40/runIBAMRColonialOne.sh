#!/bin/sh

# file: runIBAMRColonialOne.sh
# author: Olivier Mesnard (mesnard0@gwu.edu)
# brief: Runs IBAMR for an external flow (using the Constraint IB method).


#SBATCH --job-name="ibamr1k40"
#SBATCH --output=log%j.out
#SBATCH --error=log%j.err
#SBATCH --partition=short
#SBATCH --time=48:00:00
#SBATCH -n 16

MPIRUN="/c1/apps/openmpi/1.8/gcc/4.7/cpu/bin/mpirun"
IBAMR_BUILD="/groups/barbalab/src/ibamr/ibamr-objs-openmpi-1.8-gcc-4.7-opt"
PROGRAM="$IBAMR_BUILD/examples/ConstraintIB/externalFlowBluffBody2dStabilized/externalFlowBluffBody2dStabilized"

INPUT="input2d"
STRUCTURE="flyingSnake2dAoA40ds004filledInside"

time $MPIRUN $PROGRAM $INPUT --body $STRUCTURE
