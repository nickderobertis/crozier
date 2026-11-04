

import typing

from .clustering_fixed import ClusteringFixed
from .clustering_one import ClusteringOne
from .clustering_zero import ClusteringZero

Clustering = typing.Union[ClusteringZero, ClusteringOne, ClusteringFixed]
