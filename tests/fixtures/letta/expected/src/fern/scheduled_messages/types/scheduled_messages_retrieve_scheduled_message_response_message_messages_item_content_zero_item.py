

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image_source import (
    ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSource,
)


class ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    text: str
    signature: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    source: ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem = typing_extensions.Annotated[
    typing.Union[
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Text,
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Image,
    ],
    pydantic.Field(discriminator="type"),
]
