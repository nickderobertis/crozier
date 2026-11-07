

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .approval_decision import ApprovalDecision
from .user_message_content import UserMessageContent


class TurnInputItem_UserMessage(UniversalBaseModel):
    type: typing.Literal["user.message"] = "user.message"
    content: UserMessageContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TurnInputItem_UserToolApproval(UniversalBaseModel):
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


class TurnInputItem_UserToolResponse(UniversalBaseModel):
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


TurnInputItem = typing_extensions.Annotated[
    typing.Union[TurnInputItem_UserMessage, TurnInputItem_UserToolApproval, TurnInputItem_UserToolResponse],
    pydantic.Field(discriminator="type"),
]
