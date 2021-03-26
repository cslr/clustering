# Copyright 2021 Tomas Ukkonen
#
# Simple script for defining and optimizing Ising model
# 

import math

import dwavebinarycsp
import dwave.inspector
import dimod
import random
from dwave.system import EmbeddingComposite, DWaveSampler

from utilities import get_groupings, visualize_groupings, visualize_scatterplot

print("Defining model parameters..")

# build dicts (Ising model parameters)

NVAR = 50

## hi = {0: 1, 1: -1, 2: .5}
## Jji = { (0,1): .5, (1,2): .5, (0,2): -0.5 }

hi = {}
Jji = {}

for i in range(NVAR):
    hi[i] = random.random()
    for j in range(i+1,NVAR):
        Jji[(j,i)] = random.random()

print("{} parameters in Ising model.".format(str(len(Jji)+len(hi))))

# another parameter value is dimod.Vartype.BINARY for 0/1 valued variables
bqm = dimod.BinaryQuadraticModel(hi, Jji, 0.0, dimod.Vartype.SPIN)

print("Sampling model..")

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm,
                           chain_strength=4,
                           num_reads=1000,
                           label='BQM/Ising model test')

best_sample = sampleset.first.sample

print(best_sample)

