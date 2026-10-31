

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LineageImplementation(UniversalBaseModel):
    type: typing.Optional[str] = None
    name: typing.Optional[str] = None
    version: typing.Optional[str] = None
    uri: typing.Optional[str] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
