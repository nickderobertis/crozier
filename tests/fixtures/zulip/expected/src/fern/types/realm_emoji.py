

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RealmEmoji(UniversalBaseModel):
    """
    Object containing details about an emoji. It has the
    following properties:
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID for this emoji, same as the object's key.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user-friendly name for this emoji. Users in the organization
    can use this emoji by writing this name between colons (`:name :`).
    """

    source_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The path relative to the organization's URL where the
    emoji's image can be found.
    """

    still_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only non-null when the emoji's image is animated.
    
    The path relative to the organization's URL where a still
    (not animated) version of the emoji can be found. (This is
    currently always the first frame of the animation).
    
    This is useful for clients to display the emoji in contexts
    where continuously animating it would be a bad user experience
    (E.g. because it would be distracting).
    
    **Changes**: New in Zulip 5.0 (added as optional field in
    feature level 97 and then made mandatory, but nullable, in
    feature level 113).
    """

    deactivated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the emoji has been deactivated or not.
    """

    author_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user ID of the user who uploaded the custom emoji.
    Will be `null` if the uploader is unknown.
    
    **Changes**: New in Zulip 3.0 (feature level 7). Previously
    was accessible via an `author` object with an `id` field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
