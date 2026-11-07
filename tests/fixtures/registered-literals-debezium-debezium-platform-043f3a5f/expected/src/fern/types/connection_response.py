

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .type import Type


class ConnectionResponse(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    type: typing.Optional[Type] = None
    config: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
