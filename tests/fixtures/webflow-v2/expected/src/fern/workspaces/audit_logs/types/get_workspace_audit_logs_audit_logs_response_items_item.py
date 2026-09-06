

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .custom_role import CustomRole
from .get_workspace_audit_logs_audit_logs_response_items_item_actor import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemActor,
)
from .get_workspace_audit_logs_audit_logs_response_items_item_custom_role_event_sub_type import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType,
)
from .get_workspace_audit_logs_audit_logs_response_items_item_site_membership_event_sub_type import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType,
)
from .get_workspace_audit_logs_audit_logs_response_items_item_user_access_event_sub_type import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType,
)
from .get_workspace_audit_logs_audit_logs_response_items_item_workspace import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspace,
)
from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_invitation_event_sub_type import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType,
)
from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_membership_event_sub_type import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType,
)
from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_setting_event_sub_type import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType,
)
from .setting_change import SettingChange
from .site_membership import SiteMembership
from .user_access import UserAccess
from .workspace_invitation import WorkspaceInvitation
from .workspace_membership import WorkspaceMembership


class Base(UniversalBaseModel):
    timestamp: typing.Optional[dt.datetime] = None
    actor: typing.Optional[GetWorkspaceAuditLogsAuditLogsResponseItemsItemActor] = None
    workspace: typing.Optional[GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspace] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetWorkspaceAuditLogsAuditLogsResponseItemsItem_UserAccess(Base):
    event_type: typing_extensions.Annotated[
        typing.Literal["user_access"], FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")
    ] = "user_access"
    event_sub_type: typing_extensions.Annotated[
        typing.Optional[GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType],
        FieldMetadata(alias="eventSubType"),
        pydantic.Field(alias="eventSubType"),
    ] = None
    payload: typing.Optional[UserAccess] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetWorkspaceAuditLogsAuditLogsResponseItemsItem_CustomRole(Base):
    event_type: typing_extensions.Annotated[
        typing.Literal["custom_role"], FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")
    ] = "custom_role"
    event_sub_type: typing_extensions.Annotated[
        typing.Optional[GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType],
        FieldMetadata(alias="eventSubType"),
        pydantic.Field(alias="eventSubType"),
    ] = None
    payload: typing.Optional[CustomRole] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceMembership(Base):
    event_type: typing_extensions.Annotated[
        typing.Literal["workspace_membership"], FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")
    ] = "workspace_membership"
    event_sub_type: typing_extensions.Annotated[
        typing.Optional[GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType],
        FieldMetadata(alias="eventSubType"),
        pydantic.Field(alias="eventSubType"),
    ] = None
    payload: typing.Optional[WorkspaceMembership] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetWorkspaceAuditLogsAuditLogsResponseItemsItem_SiteMembership(Base):
    event_type: typing_extensions.Annotated[
        typing.Literal["site_membership"], FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")
    ] = "site_membership"
    event_sub_type: typing_extensions.Annotated[
        typing.Optional[GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType],
        FieldMetadata(alias="eventSubType"),
        pydantic.Field(alias="eventSubType"),
    ] = None
    payload: typing.Optional[SiteMembership] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceInvitation(Base):
    event_type: typing_extensions.Annotated[
        typing.Literal["workspace_invitation"], FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")
    ] = "workspace_invitation"
    event_sub_type: typing_extensions.Annotated[
        typing.Optional[GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType],
        FieldMetadata(alias="eventSubType"),
        pydantic.Field(alias="eventSubType"),
    ] = None
    payload: typing.Optional[WorkspaceInvitation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceSetting(Base):
    event_type: typing_extensions.Annotated[
        typing.Literal["workspace_setting"], FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")
    ] = "workspace_setting"
    event_sub_type: typing_extensions.Annotated[
        typing.Optional[GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType],
        FieldMetadata(alias="eventSubType"),
        pydantic.Field(alias="eventSubType"),
    ] = None
    payload: typing.Optional[SettingChange] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GetWorkspaceAuditLogsAuditLogsResponseItemsItem = typing_extensions.Annotated[
    typing.Union[
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_UserAccess,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_CustomRole,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceMembership,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_SiteMembership,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceInvitation,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceSetting,
    ],
    pydantic.Field(discriminator="event_type"),
]
