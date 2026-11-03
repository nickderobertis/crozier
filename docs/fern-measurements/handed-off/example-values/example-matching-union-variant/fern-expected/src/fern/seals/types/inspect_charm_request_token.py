

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InspectCharmRequestToken_Wax(UniversalBaseModel):
    format: typing.Literal["wax"] = "wax"
    colour: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class InspectCharmRequestToken_Charm(UniversalBaseModel):
    format: typing.Literal["charm"] = "charm"
    charm: typing.Any
    motto: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InspectCharmRequestToken = typing_extensions.Annotated[
    typing.Union[InspectCharmRequestToken_Wax, InspectCharmRequestToken_Charm], pydantic.Field(discriminator="format")
]
