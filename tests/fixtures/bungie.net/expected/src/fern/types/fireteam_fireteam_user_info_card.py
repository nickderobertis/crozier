

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FireteamFireteamUserInfoCard(UniversalBaseModel):
    fireteam_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="FireteamDisplayName")
    ] = None
    fireteam_membership_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="FireteamMembershipType")
    ] = None
    applicable_membership_types: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="applicableMembershipTypes")
    ] = pydantic.Field(default=None)
    """
    The list of Membership Types indicating the platforms on which this Membership can be used.
     Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
    """

    bungie_global_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bungieGlobalDisplayName")
    ] = pydantic.Field(default=None)
    """
    The bungie global display name, if set.
    """

    bungie_global_display_name_code: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bungieGlobalDisplayNameCode")
    ] = pydantic.Field(default=None)
    """
    The bungie global display name code, if set.
    """

    cross_save_override: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="crossSaveOverride")] = (
        pydantic.Field(default=None)
    )
    """
    If there is a cross save override in effect, this value will tell you the type that is overridding this one.
    """

    display_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="displayName")] = (
        pydantic.Field(default=None)
    )
    """
    Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
    """

    icon_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="iconPath")] = pydantic.Field(
        default=None
    )
    """
    URL the Icon if available.
    """

    is_public: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isPublic")] = pydantic.Field(
        default=None
    )
    """
    If True, this is a public user membership.
    """

    membership_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipId")] = (
        pydantic.Field(default=None)
    )
    """
    Membership ID as they user is known in the Accounts service
    """

    membership_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipType")] = (
        pydantic.Field(default=None)
    )
    """
    Type of the membership. Not necessarily the native type.
    """

    supplemental_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supplementalDisplayName")
    ] = pydantic.Field(default=None)
    """
    A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
