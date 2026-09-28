

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timestamp import Timestamp


class TimestampResMember(UniversalBaseModel):
    invited: typing.Optional[Timestamp] = None
    joined: typing.Optional[Timestamp] = None
    left: typing.Optional[Timestamp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
