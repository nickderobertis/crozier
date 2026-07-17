

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_inventory_destiny_platform_silver_component import (
    DestinyComponentsInventoryDestinyPlatformSilverComponent,
)


class DestinyResponsesDestinyProfileUserInfoCard(UniversalBaseModel):
    applicable_membership_types: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="applicableMembershipTypes"),
        pydantic.Field(
            alias="applicableMembershipTypes",
            description="The list of Membership Types indicating the platforms on which this Membership can be used.\r\n Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list",
        ),
    ] = None
    """
    The list of Membership Types indicating the platforms on which this Membership can be used.
     Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
    """

    bungie_global_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bungieGlobalDisplayName"),
        pydantic.Field(alias="bungieGlobalDisplayName", description="The bungie global display name, if set."),
    ] = None
    """
    The bungie global display name, if set.
    """

    bungie_global_display_name_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bungieGlobalDisplayNameCode"),
        pydantic.Field(alias="bungieGlobalDisplayNameCode", description="The bungie global display name code, if set."),
    ] = None
    """
    The bungie global display name code, if set.
    """

    cross_save_override: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="crossSaveOverride"),
        pydantic.Field(
            alias="crossSaveOverride",
            description="If there is a cross save override in effect, this value will tell you the type that is overridding this one.",
        ),
    ] = None
    """
    If there is a cross save override in effect, this value will tell you the type that is overridding this one.
    """

    date_last_played: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="dateLastPlayed"), pydantic.Field(alias="dateLastPlayed")
    ] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(
            alias="displayName",
            description="Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.",
        ),
    ] = None
    """
    Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
    """

    icon_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="iconPath"),
        pydantic.Field(alias="iconPath", description="URL the Icon if available."),
    ] = None
    """
    URL the Icon if available.
    """

    is_cross_save_primary: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCrossSavePrimary"),
        pydantic.Field(
            alias="isCrossSavePrimary",
            description='If true, this account is hooked up as the "Primary" cross save account for one or more platforms.',
        ),
    ] = None
    """
    If true, this account is hooked up as the "Primary" cross save account for one or more platforms.
    """

    is_overridden: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isOverridden"),
        pydantic.Field(
            alias="isOverridden",
            description="If this profile is being overridden/obscured by Cross Save, this will be set to true. We will still return the profile for display purposes where users need to know the info: it is up to any given area of the app/site to determine if this profile should still be shown.",
        ),
    ] = None
    """
    If this profile is being overridden/obscured by Cross Save, this will be set to true. We will still return the profile for display purposes where users need to know the info: it is up to any given area of the app/site to determine if this profile should still be shown.
    """

    is_public: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPublic"),
        pydantic.Field(alias="isPublic", description="If True, this is a public user membership."),
    ] = None
    """
    If True, this is a public user membership.
    """

    membership_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="membershipId"),
        pydantic.Field(alias="membershipId", description="Membership ID as they user is known in the Accounts service"),
    ] = None
    """
    Membership ID as they user is known in the Accounts service
    """

    membership_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="membershipType"),
        pydantic.Field(alias="membershipType", description="Type of the membership. Not necessarily the native type."),
    ] = None
    """
    Type of the membership. Not necessarily the native type.
    """

    platform_silver: typing_extensions.Annotated[
        typing.Optional[DestinyComponentsInventoryDestinyPlatformSilverComponent],
        FieldMetadata(alias="platformSilver"),
        pydantic.Field(
            alias="platformSilver",
            description="This is the silver available on this Profile across any platforms on which they have purchased silver.\r\n This is only available if you are requesting yourself.",
        ),
    ] = None
    """
    This is the silver available on this Profile across any platforms on which they have purchased silver.
     This is only available if you are requesting yourself.
    """

    supplemental_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="supplementalDisplayName"),
        pydantic.Field(
            alias="supplementalDisplayName",
            description="A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.",
        ),
    ] = None
    """
    A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.
    """

    unpaired_game_versions: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unpairedGameVersions"),
        pydantic.Field(
            alias="unpairedGameVersions",
            description="If this profile is not in a cross save pairing, this will return the game versions that we believe this profile has access to.\r\n For the time being, we will not return this information for any membership that is in a cross save pairing. The gist is that, once the pairing occurs, we do not currently have a consistent way to get that information for the profile's original Platform, and thus gameVersions would be too inconsistent (based on the last platform they happened to play on) for the info to be useful.\r\n If we ever can get this data, this field will be deprecated and replaced with data on the DestinyLinkedProfileResponse itself, with game versions per linked Platform. But since we can't get that, we have this as a stop-gap measure for getting the data in the only situation that we currently need it.",
        ),
    ] = None
    """
    If this profile is not in a cross save pairing, this will return the game versions that we believe this profile has access to.
     For the time being, we will not return this information for any membership that is in a cross save pairing. The gist is that, once the pairing occurs, we do not currently have a consistent way to get that information for the profile's original Platform, and thus gameVersions would be too inconsistent (based on the last platform they happened to play on) for the info to be useful.
     If we ever can get this data, this field will be deprecated and replaced with data on the DestinyLinkedProfileResponse itself, with game versions per linked Platform. But since we can't get that, we have this as a stop-gap measure for getting the data in the only situation that we currently need it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
