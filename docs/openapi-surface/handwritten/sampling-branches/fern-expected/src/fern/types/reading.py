

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Reading(UniversalBaseModel):
    index: typing.Optional[int] = None
    rate: typing.Optional[int] = pydantic.Field(default=None)
    """
    Recorded sampling rate.
    """

    unit: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
