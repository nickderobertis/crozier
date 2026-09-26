

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_status_reaction_type import UserStatusReactionType


class UserStatus(UniversalBaseModel):
    away: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If present, the user has marked themself "away".
    
    **Changes**: Deprecated in Zulip 6.0 (feature level 148);
    starting with that feature level, `away` is a legacy way to
    access the user's `presence_enabled` setting, with
    `away = !presence_enabled`. To be removed in a future release.
    """

    status_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    If present, the text content of the user's status message.
    """

    emoji_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    If present, the name for the emoji to associate with the user's status.
    
    **Changes**: New in Zulip 5.0 (feature level 86).
    """

    emoji_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    If present, a unique identifier, defining the specific emoji codepoint
    requested, within the namespace of the `reaction_type`.
    
    **Changes**: New in Zulip 5.0 (feature level 86).
    """

    reaction_type: typing.Optional[UserStatusReactionType] = pydantic.Field(default=None)
    """
    If present, a string indicating the type of emoji. Each emoji
    `reaction_type` has an independent namespace for values of `emoji_code`.
    
    Must be one of the following values:
    
    - `unicode_emoji` : In this namespace, `emoji_code` will be a
      dash-separated hex encoding of the sequence of Unicode codepoints
      that define this emoji in the Unicode specification.
    
    - `realm_emoji` : In this namespace, `emoji_code` will be the ID of
      the uploaded [custom emoji](/help/custom-emoji).
    
    - `zulip_extra_emoji` : These are special emoji included with Zulip.
      In this namespace, `emoji_code` will be the name of the emoji (e.g.
      "zulip").
    
    **Changes**: New in Zulip 5.0 (feature level 86).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
