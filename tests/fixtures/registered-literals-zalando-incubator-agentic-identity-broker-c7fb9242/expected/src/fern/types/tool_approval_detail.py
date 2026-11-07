

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_approval_detail_persistence import ToolApprovalDetailPersistence
from .tool_approval_detail_risk_level import ToolApprovalDetailRiskLevel
from .tool_approval_detail_status import ToolApprovalDetailStatus


class ToolApprovalDetail(UniversalBaseModel):
    id: str
    principal: str
    agent_id: str
    agent_display_name: typing.Optional[str] = None
    mcp_session_id: typing.Optional[str] = None
    agent_session_id: typing.Optional[str] = None
    tool_invocation_id: typing.Optional[str] = None
    tool_name: str
    arguments: typing.Dict[str, typing.Any]
    tool_pattern: str = pydantic.Field()
    """
    Server-derived exact matcher for this approval's `tool_name`.
    """

    params_pattern: typing.Dict[str, str] = pydantic.Field()
    """
    Constrained argument names mapped to globs; absent keys are unconstrained.
    """

    pattern_preview: str = pydantic.Field()
    """
    Server-rendered representation of the approval pattern.
    """

    description: typing.Optional[str] = None
    risk_level: typing.Optional[ToolApprovalDetailRiskLevel] = None
    status: ToolApprovalDetailStatus
    persistence: typing.Optional[ToolApprovalDetailPersistence] = None
    consumed: typing.Optional[bool] = None
    approval_url: str
    created_at: dt.datetime
    approved_at: typing.Optional[dt.datetime] = None
    denied_at: typing.Optional[dt.datetime] = None
    consumed_at: typing.Optional[dt.datetime] = None
    expires_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
