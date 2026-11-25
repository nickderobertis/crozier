

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TimelineItemsItem_Message(UniversalBaseModel):
    kind: typing.Literal["message"] = "message"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TimelineItemsItem_Tool(UniversalBaseModel):
    kind: typing.Literal["tool"] = "tool"
    tool_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TimelineItemsItem_Note(UniversalBaseModel):
    kind: typing.Literal["note"] = "note"
    body: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TimelineItemsItem = typing_extensions.Annotated[
    typing.Union[TimelineItemsItem_Message, TimelineItemsItem_Tool, TimelineItemsItem_Note],
    pydantic.Field(discriminator="kind"),
]
