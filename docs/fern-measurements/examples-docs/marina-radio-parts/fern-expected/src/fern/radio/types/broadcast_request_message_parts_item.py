

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BroadcastRequestMessagePartsItem_Voice(UniversalBaseModel):
    kind: typing.Literal["voice"] = "voice"
    transcript: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class BroadcastRequestMessagePartsItem_Position(UniversalBaseModel):
    kind: typing.Literal["position"] = "position"
    fix: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


BroadcastRequestMessagePartsItem = typing_extensions.Annotated[
    typing.Union[BroadcastRequestMessagePartsItem_Voice, BroadcastRequestMessagePartsItem_Position],
    pydantic.Field(discriminator="kind"),
]
