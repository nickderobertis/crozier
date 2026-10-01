

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Holder(UniversalBaseModel):
    merged: typing.Optional[typing.List[typing.Any]] = None
    chosen: typing.Optional[typing.List[typing.Any]] = None
    either: typing.Optional[typing.List[typing.Any]] = None
    tags: typing.Optional[typing.List[typing.Any]] = None
    names: typing.Optional[typing.List[typing.Any]] = None
    ghost: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
