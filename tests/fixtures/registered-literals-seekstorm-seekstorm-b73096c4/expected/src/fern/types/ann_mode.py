

import typing

from .ann_mode_nprobe import AnnModeNprobe
from .ann_mode_nprobe_similaritythreshold import AnnModeNprobeSimilaritythreshold
from .ann_mode_similaritythreshold import AnnModeSimilaritythreshold
from .ann_mode_zero import AnnModeZero

AnnMode = typing.Union[AnnModeZero, AnnModeNprobe, AnnModeSimilaritythreshold, AnnModeNprobeSimilaritythreshold]
