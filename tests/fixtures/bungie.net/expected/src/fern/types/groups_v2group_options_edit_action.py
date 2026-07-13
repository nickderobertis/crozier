

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GroupsV2GroupOptionsEditAction(UniversalBaseModel):
    host_guided_game_permission_override: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="HostGuidedGamePermissionOverride")
    ] = pydantic.Field(default=None)
    """
    Minimum Member Level allowed to host guided games
    Always Allowed: Founder, Acting Founder, Admin
    Allowed Overrides: None, Member, Beginner
    Default is Member for clans, None for groups, although this means nothing for groups.
    """

    invite_permission_override: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="InvitePermissionOverride")
    ] = pydantic.Field(default=None)
    """
    Minimum Member Level allowed to invite new members to group
    Always Allowed: Founder, Acting Founder
    True means admins have this power, false means they don't
    Default is false for clans, true for groups.
    """

    join_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="JoinLevel")] = pydantic.Field(
        default=None
    )
    """
    Level to join a member at when accepting an invite, application, or joining an open clan
    Default is Beginner.
    """

    update_banner_permission_override: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="UpdateBannerPermissionOverride")
    ] = pydantic.Field(default=None)
    """
    Minimum Member Level allowed to update banner
    Always Allowed: Founder, Acting Founder
    True means admins have this power, false means they don't
    Default is false for clans, true for groups.
    """

    update_culture_permission_override: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="UpdateCulturePermissionOverride")
    ] = pydantic.Field(default=None)
    """
    Minimum Member Level allowed to update group culture
    Always Allowed: Founder, Acting Founder
    True means admins have this power, false means they don't
    Default is false for clans, true for groups.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
