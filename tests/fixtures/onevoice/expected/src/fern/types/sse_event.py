

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .approval_call import ApprovalCall


class SseEvent_Text(UniversalBaseModel):
    """
    Discriminated union over the per-type SSE event schemas. `type`
    is the discriminator. Wire envelope is `data: <json>\\n\\n`.
    """

    type: typing.Literal["text"] = "text"
    content: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SseEvent_ToolCall(UniversalBaseModel):
    """
    Discriminated union over the per-type SSE event schemas. `type`
    is the discriminator. Wire envelope is `data: <json>\\n\\n`.
    """

    type: typing.Literal["tool_call"] = "tool_call"
    tool_call_id: typing.Optional[str] = None
    tool_name: typing.Optional[str] = None
    tool_display_name: typing.Optional[str] = None
    tool_display_name_key: typing.Optional[str] = None
    tool_args: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SseEvent_ToolResult(UniversalBaseModel):
    """
    Discriminated union over the per-type SSE event schemas. `type`
    is the discriminator. Wire envelope is `data: <json>\\n\\n`.
    """

    type: typing.Literal["tool_result"] = "tool_result"
    tool_call_id: typing.Optional[str] = None
    tool_name: typing.Optional[str] = None
    tool_display_name: typing.Optional[str] = None
    tool_display_name_key: typing.Optional[str] = None
    result: typing.Optional[typing.Any] = None
    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SseEvent_ToolRejected(UniversalBaseModel):
    """
    Discriminated union over the per-type SSE event schemas. `type`
    is the discriminator. Wire envelope is `data: <json>\\n\\n`.
    """

    type: typing.Literal["tool_rejected"] = "tool_rejected"
    tool_call_id: typing.Optional[str] = None
    tool_name: typing.Optional[str] = None
    tool_display_name: typing.Optional[str] = None
    tool_display_name_key: typing.Optional[str] = None
    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SseEvent_ToolApprovalRequired(UniversalBaseModel):
    """
    Discriminated union over the per-type SSE event schemas. `type`
    is the discriminator. Wire envelope is `data: <json>\\n\\n`.
    """

    type: typing.Literal["tool_approval_required"] = "tool_approval_required"
    batch_id: str
    calls: typing.List[ApprovalCall]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SseEvent_Done(UniversalBaseModel):
    """
    Discriminated union over the per-type SSE event schemas. `type`
    is the discriminator. Wire envelope is `data: <json>\\n\\n`.
    """

    type: typing.Literal["done"] = "done"
    content: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SseEvent_Error(UniversalBaseModel):
    """
    Discriminated union over the per-type SSE event schemas. `type`
    is the discriminator. Wire envelope is `data: <json>\\n\\n`.
    """

    type: typing.Literal["error"] = "error"
    code: typing.Optional[str] = None
    content: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SseEvent = typing_extensions.Annotated[
    typing.Union[
        SseEvent_Text,
        SseEvent_ToolCall,
        SseEvent_ToolResult,
        SseEvent_ToolRejected,
        SseEvent_ToolApprovalRequired,
        SseEvent_Done,
        SseEvent_Error,
    ],
    pydantic.Field(discriminator="type"),
]
