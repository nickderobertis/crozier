

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MastheadSettings(UniversalBaseModel):
    background: typing.Optional[str] = None
    background_color: typing.Optional[str] = None
    color: typing.Optional[str] = None
    columns: typing.Optional[int] = None
    description: typing.Optional[str] = None
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
