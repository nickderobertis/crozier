

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .log_trace_span_cost import LogTraceSpanCost
from .log_trace_span_tokens import LogTraceSpanTokens
from .log_trace_span_tool_calls_item import LogTraceSpanToolCallsItem


class LogTraceSpan(UniversalBaseModel):
    """
    One recursive operation span in a workflow execution trace.
    """

    id: str = pydantic.Field()
    """
    Trace-span identifier.
    """

    name: str = pydantic.Field()
    """
    Trace-span name.
    """

    type: str = pydantic.Field()
    """
    Trace-span category.
    """

    duration: typing.Optional[float] = pydantic.Field(default=None)
    """
    Current trace-span duration in milliseconds.
    """

    duration_ms: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="durationMs"),
        pydantic.Field(
            alias="durationMs",
            description="Compatibility field for span duration in milliseconds. Read `duration` for current trace spans.",
        ),
    ] = None
    """
    Compatibility field for span duration in milliseconds. Read `duration` for current trace spans.
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startTime"),
        pydantic.Field(alias="startTime", description="ISO 8601 span start timestamp."),
    ] = None
    """
    ISO 8601 span start timestamp.
    """

    end_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endTime"),
        pydantic.Field(alias="endTime", description="ISO 8601 span end timestamp."),
    ] = None
    """
    ISO 8601 span end timestamp.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Trace-span status.
    """

    error_handled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="errorHandled"),
        pydantic.Field(alias="errorHandled", description="Whether the recorded error was handled."),
    ] = None
    """
    Whether the recorded error was handled.
    """

    error_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="errorType"),
        pydantic.Field(alias="errorType", description="Recorded error type."),
    ] = None
    """
    Recorded error type.
    """

    error_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="errorMessage"),
        pydantic.Field(alias="errorMessage", description="Recorded error message."),
    ] = None
    """
    Recorded error message.
    """

    block_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="blockId"),
        pydantic.Field(alias="blockId", description="Workflow block associated with the span."),
    ] = None
    """
    Workflow block associated with the span.
    """

    input: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Input captured for the traced operation.
    """

    output: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Output captured for the traced operation.
    """

    tokens: typing.Optional[LogTraceSpanTokens] = pydantic.Field(default=None)
    """
    Token usage attributed to the span.
    """

    cost: typing.Optional[LogTraceSpanCost] = pydantic.Field(default=None)
    """
    Cost attributed to the span.
    """

    relative_start_ms: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="relativeStartMs"),
        pydantic.Field(alias="relativeStartMs", description="Offset from the root span in milliseconds."),
    ] = None
    """
    Offset from the root span in milliseconds.
    """

    tool_calls: typing_extensions.Annotated[
        typing.Optional[typing.List[LogTraceSpanToolCallsItem]],
        FieldMetadata(alias="toolCalls"),
        pydantic.Field(alias="toolCalls", description="Tool calls recorded by the span."),
    ] = None
    """
    Tool calls recorded by the span.
    """

    children: typing.Optional[typing.List["LogTraceSpan"]] = pydantic.Field(default=None)
    """
    Nested child trace spans.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(LogTraceSpan)
