

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .emoji_reaction_reaction_type import EmojiReactionReactionType


class EmojiReaction(UniversalBaseModel):
    emoji_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier, defining the specific emoji codepoint requested,
    within the namespace of the `reaction_type`.
    """

    emoji_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the emoji.
    """

    reaction_type: typing.Optional[EmojiReactionReactionType] = pydantic.Field(default=None)
    """
    A string indicating the type of emoji. Each emoji `reaction_type`
    has an independent namespace for values of `emoji_code`.
    
    Must be one of the following values:
    
    - `unicode_emoji` : In this namespace, `emoji_code` will be a
      dash-separated hex encoding of the sequence of Unicode codepoints
      that define this emoji in the Unicode specification.
    
    - `realm_emoji` : In this namespace, `emoji_code` will be the ID of
      the uploaded [custom emoji](/help/custom-emoji).
    
    - `zulip_extra_emoji` : These are special emoji included with Zulip.
      In this namespace, `emoji_code` will be the name of the emoji (e.g.
      "zulip").
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who added the reaction.
    
    **Changes**: New in Zulip 3.0 (feature level 2), which
    deprecated the `user` object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
