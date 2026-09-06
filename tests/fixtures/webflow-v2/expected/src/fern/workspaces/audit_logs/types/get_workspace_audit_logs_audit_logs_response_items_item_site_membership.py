

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_workspace_audit_logs_audit_logs_response_items_item_site_membership_event_sub_type import (
    GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType,
)
from .site_membership import SiteMembership


class GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembership(UniversalBaseModel):
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
