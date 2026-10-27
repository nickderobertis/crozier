

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .team_discovery_settings import TeamDiscoverySettings
from .team_fun_settings import TeamFunSettings
from .team_guest_settings import TeamGuestSettings
from .team_member_settings import TeamMemberSettings
from .team_messaging_settings import TeamMessagingSettings
from .team_specialization import TeamSpecialization
from .team_summary import TeamSummary
from .team_visibility import TeamVisibility


class Team(UniversalBaseModel):
    odata_context: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@odata.context"), pydantic.Field(alias="@odata.context")
    ] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the team
    """

    created_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdDateTime"), pydantic.Field(alias="createdDateTime")
    ] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name of the team"),
    ] = None
    """
    Display name of the team
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the team
    """

    internal_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="internalId"), pydantic.Field(alias="internalId")
    ] = None
    classification: typing.Optional[str] = None
    specialization: typing.Optional[TeamSpecialization] = None
    visibility: typing.Optional[TeamVisibility] = None
    web_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webUrl"), pydantic.Field(alias="webUrl")
    ] = None
    is_archived: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isArchived"), pydantic.Field(alias="isArchived")
    ] = None
    is_membership_limited_to_owners: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isMembershipLimitedToOwners"),
        pydantic.Field(alias="isMembershipLimitedToOwners"),
    ] = None
    discovery_settings: typing_extensions.Annotated[
        typing.Optional[TeamDiscoverySettings],
        FieldMetadata(alias="discoverySettings"),
        pydantic.Field(alias="discoverySettings"),
    ] = None
    member_settings: typing_extensions.Annotated[
        typing.Optional[TeamMemberSettings],
        FieldMetadata(alias="memberSettings"),
        pydantic.Field(alias="memberSettings"),
    ] = None
    guest_settings: typing_extensions.Annotated[
        typing.Optional[TeamGuestSettings], FieldMetadata(alias="guestSettings"), pydantic.Field(alias="guestSettings")
    ] = None
    messaging_settings: typing_extensions.Annotated[
        typing.Optional[TeamMessagingSettings],
        FieldMetadata(alias="messagingSettings"),
        pydantic.Field(alias="messagingSettings"),
    ] = None
    fun_settings: typing_extensions.Annotated[
        typing.Optional[TeamFunSettings], FieldMetadata(alias="funSettings"), pydantic.Field(alias="funSettings")
    ] = None
    summary: typing.Optional[TeamSummary] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
