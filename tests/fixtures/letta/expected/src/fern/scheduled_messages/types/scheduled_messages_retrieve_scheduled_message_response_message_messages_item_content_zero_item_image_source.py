

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image_source_type import (
    ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSourceType,
)


class ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSource(
    UniversalBaseModel
):
    data: str
    media_type: str
    detail: typing.Optional[str] = None
    type: typing.Optional[
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSourceType
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
