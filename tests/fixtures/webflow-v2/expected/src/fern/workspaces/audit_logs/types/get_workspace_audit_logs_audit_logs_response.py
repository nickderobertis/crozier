

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_workspace_audit_logs_audit_logs_response_items_item import GetWorkspaceAuditLogsAuditLogsResponseItemsItem
from .get_workspace_audit_logs_audit_logs_response_pagination import GetWorkspaceAuditLogsAuditLogsResponsePagination


class GetWorkspaceAuditLogsAuditLogsResponse(UniversalBaseModel):
    items: typing.Optional[typing.List[GetWorkspaceAuditLogsAuditLogsResponseItemsItem]] = None
    pagination: typing.Optional[GetWorkspaceAuditLogsAuditLogsResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
