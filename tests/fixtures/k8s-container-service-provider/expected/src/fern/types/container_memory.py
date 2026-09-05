

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContainerMemory(UniversalBaseModel):
    """
    Memory resource constraints
    """

    min: str = pydantic.Field()
    """
    Minimum guaranteed memory with unit (e.g., "1GB", "2GB")
    """

    max: str = pydantic.Field()
    """
    Maximum allowed memory with unit (e.g., "2GB", "4GB")
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
