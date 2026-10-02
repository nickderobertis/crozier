

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RouteTo_App(UniversalBaseModel):
    type: typing.Literal["app"] = "app"
    user: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RouteTo_Phone(UniversalBaseModel):
    type: typing.Literal["phone"] = "phone"
    number: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RouteTo = typing_extensions.Annotated[typing.Union[RouteTo_App, RouteTo_Phone], pydantic.Field(discriminator="type")]
