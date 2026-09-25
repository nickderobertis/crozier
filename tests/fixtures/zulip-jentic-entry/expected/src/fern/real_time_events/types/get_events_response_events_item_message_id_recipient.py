

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_events_response_events_item_message_id_recipient_type import GetEventsResponseEventsItemMessageIdRecipientType


class GetEventsResponseEventsItemMessageIdRecipient(UniversalBaseModel):
    """
    Object containing details about recipients of message edit typing notification.
    """

    type: typing.Optional[GetEventsResponseEventsItemMessageIdRecipientType] = pydantic.Field(default=None)
    """
    Type of message being composed. Must be `"channel"` or `"direct"`.
    """

    channel_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present if `type` is `"channel"`.
    
    The unique ID of the channel to which message is being edited.
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if `type` is `"channel"`.
    
    Topic within the channel where the message is being edited.
    """

    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Present only if `type` is `direct`.
    
    The user IDs of every recipient of this direct message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
