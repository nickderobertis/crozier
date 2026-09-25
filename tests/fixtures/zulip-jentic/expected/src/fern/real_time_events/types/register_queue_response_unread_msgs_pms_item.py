

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseUnreadMsgsPmsItem(UniversalBaseModel):
    other_user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user ID of the other participant in this one-on-one direct
    message conversation. Will be the current user's ID for messages
    that they sent in a one-on-one direct message conversation with
    themself.
    
    **Changes**: New in Zulip 5.0 (feature level 119), replacing
    the less clearly named `sender_id` field.
    """

    sender_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Old name for the `other_user_id` field. Clients should access
    this field in Zulip server versions that do not yet support
    `other_user_id`.
    
    **Changes**: Deprecated in Zulip 5.0 (feature level 119).
    We expect to provide a next version of the full `unread_msgs`
    API before removing this legacy name.
    """

    unread_message_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The message IDs of the recent unread direct messages sent
    by either user in this one-on-one direct message conversation,
    sorted in ascending order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
