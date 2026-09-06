

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WpLinkDto(UniversalBaseModel):
    height: typing.Optional[int] = None
    href: typing.Optional[str] = None
    properties: typing.Dict[str, typing.Dict[str, typing.Any]]
    rel: typing.Optional[str] = None
    templated: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    type: typing.Optional[str] = None
    width: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
