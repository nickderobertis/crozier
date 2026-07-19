

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .letta_schemas_letta_message_tool_return_status import LettaSchemasLettaMessageToolReturnStatus
from .letta_schemas_letta_message_tool_return_tool_return import LettaSchemasLettaMessageToolReturnToolReturn


class ApprovalResponseMessageApprovalsItem_Approval(UniversalBaseModel):
    type: typing.Literal["approval"] = "approval"
    tool_call_id: str
    approve: bool
    reason: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ApprovalResponseMessageApprovalsItem_Tool(UniversalBaseModel):
    type: typing.Literal["tool"] = "tool"
    tool_return: LettaSchemasLettaMessageToolReturnToolReturn
    status: LettaSchemasLettaMessageToolReturnStatus
    tool_call_id: str
    stdout: typing.Optional[typing.List[str]] = None
    stderr: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ApprovalResponseMessageApprovalsItem = typing_extensions.Annotated[
    typing.Union[ApprovalResponseMessageApprovalsItem_Approval, ApprovalResponseMessageApprovalsItem_Tool],
    pydantic.Field(discriminator="type"),
]
