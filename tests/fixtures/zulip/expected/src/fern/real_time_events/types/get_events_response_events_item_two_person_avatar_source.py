

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemTwoPersonAvatarSource(UniversalBaseModel):
    """
    When a user changes their avatar.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who is affected by this change.
    """

    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the new avatar for the user.
    """

    avatar_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new avatar data source type for the user. Valid values are:
    
    - "G" = Hosted by Gravatar
    - "J" = Generated using Jdenticon
    - "U" = Uploaded by user
    
    **Changes**: The "J" value is new in Zulip 12.0 (feature level 466).
    """

    avatar_url_medium: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new medium-size avatar URL for user.
    """

    avatar_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version number for the user's avatar. This is useful
    for cache-busting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
