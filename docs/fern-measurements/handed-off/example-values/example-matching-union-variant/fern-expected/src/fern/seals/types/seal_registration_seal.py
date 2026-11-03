

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SealRegistrationSeal_Wax(UniversalBaseModel):
    format: typing.Literal["wax"] = "wax"
    colour: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SealRegistrationSeal_Stamp(UniversalBaseModel):
    format: typing.Literal["stamp"] = "stamp"
    stamp_id: str
    inked: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SealRegistrationSeal = typing_extensions.Annotated[
    typing.Union[SealRegistrationSeal_Wax, SealRegistrationSeal_Stamp], pydantic.Field(discriminator="format")
]
