

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContainerCpu(UniversalBaseModel):
    """
    CPU resource constraints
    """

    min: int = pydantic.Field()
    """
    Minimum guaranteed CPU cores
    """

    max: int = pydantic.Field()
    """
    Maximum allowed CPU cores
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
