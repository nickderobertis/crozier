

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Member(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    email: typing.Optional[str] = None
    role: typing.Optional[str] = None
    joined_at: typing.Optional[dt.datetime] = None
    level: typing.Optional[int] = None
    points: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
