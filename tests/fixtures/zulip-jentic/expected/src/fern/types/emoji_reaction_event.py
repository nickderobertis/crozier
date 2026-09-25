

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .emoji_base import EmojiBase
from .emoji_reaction_event_user import EmojiReactionEventUser


class EmojiReactionEvent(EmojiBase):
    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who added the reaction.
    
    **Changes**: New in Zulip 3.0 (feature level 2). The `user`
    object is deprecated and will be removed in the future.
    """

    user: typing.Optional[EmojiReactionEventUser] = pydantic.Field(default=None)
    """
    Dictionary with data on the user who added the
    reaction, including the user ID as the `user_id`
    field.
    
    **Changes**: This field was re-added in Zulip 10.0 (feature
    level 339) after having been removed in Zulip 10.0 (feature
    level 328). It remains deprecated; it was re-added because the
    React Native mobile app was still using it.
    
    **Deprecated** and to be removed in a future release once core
    clients have migrated to use the adjacent `user_id` field, which
    was introduced in Zulip 3.0 (feature level 2). Clients
    supporting older Zulip server versions should use the user ID
    mentioned in the description above as they would the `user_id`
    field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
