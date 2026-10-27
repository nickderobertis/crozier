

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_files_folder import ChannelFilesFolder
from .channel_membership_type import ChannelMembershipType
from .channel_summary import ChannelSummary


class Channel(UniversalBaseModel):
    odata_context: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="@odata.context"), pydantic.Field(alias="@odata.context")
    ] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the channel
    """

    created_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdDateTime"), pydantic.Field(alias="createdDateTime")
    ] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Channel name as it will appear to the user"),
    ] = None
    """
    Channel name as it will appear to the user
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional textual description for the channel
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address for sending messages to the channel
    """

    web_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webUrl"),
        pydantic.Field(alias="webUrl", description="A hyperlink to the channel in Microsoft Teams"),
    ] = None
    """
    A hyperlink to the channel in Microsoft Teams
    """

    membership_type: typing_extensions.Annotated[
        typing.Optional[ChannelMembershipType],
        FieldMetadata(alias="membershipType"),
        pydantic.Field(alias="membershipType", description="The type of the channel"),
    ] = None
    """
    The type of the channel
    """

    is_archived: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isArchived"),
        pydantic.Field(alias="isArchived", description="Indicates whether the channel is archived"),
    ] = None
    """
    Indicates whether the channel is archived
    """

    is_favorite_by_default: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isFavoriteByDefault"),
        pydantic.Field(
            alias="isFavoriteByDefault",
            description="Indicates whether the channel should be marked as favorite by default",
        ),
    ] = None
    """
    Indicates whether the channel should be marked as favorite by default
    """

    tenant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tenantId"),
        pydantic.Field(alias="tenantId", description="The ID of the Azure AD tenant"),
    ] = None
    """
    The ID of the Azure AD tenant
    """

    summary: typing.Optional[ChannelSummary] = None
    files_folder: typing_extensions.Annotated[
        typing.Optional[ChannelFilesFolder], FieldMetadata(alias="filesFolder"), pydantic.Field(alias="filesFolder")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
