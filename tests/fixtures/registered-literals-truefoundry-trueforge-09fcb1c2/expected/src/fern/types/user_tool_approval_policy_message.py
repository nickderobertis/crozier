

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_approval_policy_item import ToolApprovalPolicyItem


class UserToolApprovalPolicyMessage(UniversalBaseModel):
    policies: typing.List[ToolApprovalPolicyItem] = pydantic.Field()
    """
    One or more (server_name, name) policy entries.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
