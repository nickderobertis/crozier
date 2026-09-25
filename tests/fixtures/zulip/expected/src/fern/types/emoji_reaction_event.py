

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .emoji_base import EmojiBase


class EmojiReactionEvent(EmojiBase):
    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who added the reaction.
    
    **Changes**: In Zulip 12.0 (feature level 484),
    the deprecated `user` object field was removed. It contained
    the following properties: `user_id`, `email`,
    `full_name`, and `is_mirror_dummy`.
    
    Previously, in Zulip 10.0 (feature level 339), this
    object was temporarily re-added to support older mobile
    clients, after having been removed in Zulip 10.0
    (feature level 328).
    
    New in Zulip 3.0 (feature level 2).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
