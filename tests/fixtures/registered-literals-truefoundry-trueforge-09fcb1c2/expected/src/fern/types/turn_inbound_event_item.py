

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .approval_decision import ApprovalDecision
from .tool_approval_policy_item import ToolApprovalPolicyItem


class TurnInboundEventItem_UserMcpAuthContinue(UniversalBaseModel):
    type: typing.Literal["user.mcp_auth_continue"] = "user.mcp_auth_continue"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TurnInboundEventItem_UserToolApproval(UniversalBaseModel):
    type: typing.Literal["user.tool_approval"] = "user.tool_approval"
    approval: ApprovalDecision
    thread_id: str
    tool_call_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TurnInboundEventItem_UserToolApprovalPolicy(UniversalBaseModel):
    type: typing.Literal["user.tool_approval_policy"] = "user.tool_approval_policy"
    policies: typing.List[ToolApprovalPolicyItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TurnInboundEventItem_UserToolResponse(UniversalBaseModel):
    type: typing.Literal["user.tool_response"] = "user.tool_response"
    content: str
    thread_id: str
    tool_call_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TurnInboundEventItem = typing_extensions.Annotated[
    typing.Union[
        TurnInboundEventItem_UserMcpAuthContinue,
        TurnInboundEventItem_UserToolApproval,
        TurnInboundEventItem_UserToolApprovalPolicy,
        TurnInboundEventItem_UserToolResponse,
    ],
    pydantic.Field(discriminator="type"),
]
