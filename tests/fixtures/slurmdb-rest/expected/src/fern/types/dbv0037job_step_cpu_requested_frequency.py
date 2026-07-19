

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037JobStepCpuRequestedFrequency(UniversalBaseModel):
    """
    CPU frequency requested
    """

    min: typing.Optional[int] = pydantic.Field(default=None)
    """
    Min CPU frequency
    """

    max: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max CPU frequency
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
