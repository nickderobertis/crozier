

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DiskAutoscaleConfigOutput(UniversalBaseModel):
    growth_percent: typing.Optional[int] = pydantic.Field(default=None)
    """
    Growth percentage for disk autoscaling
    """

    min_increment_gb: typing.Optional[int] = pydantic.Field(default=None)
    """
    Minimum increment size for disk autoscaling in GB
    """

    max_size_gb: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum limit the disk size will grow to in GB
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
