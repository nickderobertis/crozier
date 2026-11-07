

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_approval_policy_item_action import ToolApprovalPolicyItemAction


class ToolApprovalPolicyItem(UniversalBaseModel):
    action: ToolApprovalPolicyItemAction
    name: str = pydantic.Field()
    """
    Tool name on that server.
    """

    server_name: str = pydantic.Field()
    """
    MCP server name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
