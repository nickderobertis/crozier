

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VerifyBadgeRequestBadge_Tin(UniversalBaseModel):
    kind: typing.Literal["tin"] = "tin"
    serial: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class VerifyBadgeRequestBadge_Copper(UniversalBaseModel):
    kind: typing.Literal["copper"] = "copper"
    serial: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


VerifyBadgeRequestBadge = typing_extensions.Annotated[
    typing.Union[VerifyBadgeRequestBadge_Tin, VerifyBadgeRequestBadge_Copper], pydantic.Field(discriminator="kind")
]
