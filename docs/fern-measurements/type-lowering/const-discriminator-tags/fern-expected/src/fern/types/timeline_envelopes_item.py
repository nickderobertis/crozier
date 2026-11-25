

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TimelineEnvelopesItem_Approval(UniversalBaseModel):
    type: typing.Literal["approval"] = "approval"
    approved: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TimelineEnvelopesItem_Tool(UniversalBaseModel):
    type: typing.Literal["tool"] = "tool"
    output: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TimelineEnvelopesItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TimelineEnvelopesItem_Ping(UniversalBaseModel):
    type: typing.Literal["ping"] = "ping"
    sent_at: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TimelineEnvelopesItem = typing_extensions.Annotated[
    typing.Union[
        TimelineEnvelopesItem_Approval,
        TimelineEnvelopesItem_Tool,
        TimelineEnvelopesItem_Text,
        TimelineEnvelopesItem_Ping,
    ],
    pydantic.Field(discriminator="type"),
]
