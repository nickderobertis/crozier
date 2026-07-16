

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cluster_status_label import ClusterStatusLabel
from .cluster_status_value import ClusterStatusValue


class ClusterStatus(UniversalBaseModel):
    label: ClusterStatusLabel
    value: ClusterStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
