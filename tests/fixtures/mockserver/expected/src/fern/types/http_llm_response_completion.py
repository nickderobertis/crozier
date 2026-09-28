

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .http_llm_response_completion_streaming_physics import HttpLlmResponseCompletionStreamingPhysics
from .http_llm_response_completion_tool_calls_item import HttpLlmResponseCompletionToolCallsItem
from .http_llm_response_completion_usage import HttpLlmResponseCompletionUsage


class HttpLlmResponseCompletion(UniversalBaseModel):
    text: typing.Optional[str] = None
    tool_calls: typing_extensions.Annotated[
        typing.Optional[typing.List[HttpLlmResponseCompletionToolCallsItem]],
        FieldMetadata(alias="toolCalls"),
        pydantic.Field(alias="toolCalls"),
    ] = None
    stop_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stopReason"), pydantic.Field(alias="stopReason")
    ] = None
    usage: typing.Optional[HttpLlmResponseCompletionUsage] = None
    streaming: typing.Optional[bool] = None
    output_schema: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="outputSchema"), pydantic.Field(alias="outputSchema")
    ] = None
    enforce_output_schema: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enforceOutputSchema"), pydantic.Field(alias="enforceOutputSchema")
    ] = None
    tool_choice: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="toolChoice"), pydantic.Field(alias="toolChoice")
    ] = None
    reasoning_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="reasoningText"), pydantic.Field(alias="reasoningText")
    ] = None
    reasoning_signature: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="reasoningSignature"), pydantic.Field(alias="reasoningSignature")
    ] = None
    model: typing.Optional[str] = None
    streaming_physics: typing_extensions.Annotated[
        typing.Optional[HttpLlmResponseCompletionStreamingPhysics],
        FieldMetadata(alias="streamingPhysics"),
        pydantic.Field(alias="streamingPhysics"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
