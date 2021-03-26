# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import math

import dwavebinarycsp
import dwave.inspector
import dimod
from dwave.system import EmbeddingComposite, DWaveSampler

from utilities import get_groupings, visualize_groupings, visualize_scatterplot


# build dicts (Ising model parameters)

hj = {0: 1, 1: -1, 2: .5}
Jij = { (0,1): .5, (1,2): .5, (0,2): -0.5 }

bqm = dimod.BinaryQuadraticModel(hj, Jij, 0.0, dimod.Vartype.SPIN)


sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm,
                           chain_strength=4,
                           num_reads=1000,
                           label='BQM/Ising model test')

best_sample = sampleset.first.sample

print(best_sample)

