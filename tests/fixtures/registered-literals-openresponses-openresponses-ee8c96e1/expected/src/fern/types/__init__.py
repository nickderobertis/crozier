



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .allowed_tool_choice import AllowedToolChoice
    from .allowed_tool_choice_type import AllowedToolChoiceType
    from .allowed_tools_param import AllowedToolsParam
    from .allowed_tools_param_mode import AllowedToolsParamMode
    from .allowed_tools_param_type import AllowedToolsParamType
    from .annotation import Annotation
    from .assistant_message_item_param import AssistantMessageItemParam
    from .assistant_message_item_param_content import AssistantMessageItemParamContent
    from .assistant_message_item_param_content_zero_item import (
        AssistantMessageItemParamContentZeroItem,
        AssistantMessageItemParamContentZeroItem_OutputText,
        AssistantMessageItemParamContentZeroItem_Refusal,
    )
    from .assistant_message_item_param_role import AssistantMessageItemParamRole
    from .assistant_message_item_param_type import AssistantMessageItemParamType
    from .create_response_body_input import CreateResponseBodyInput
    from .create_response_body_reasoning import CreateResponseBodyReasoning
    from .create_response_body_reasoning_summary import CreateResponseBodyReasoningSummary
    from .create_response_body_service_tier import CreateResponseBodyServiceTier
    from .create_response_body_stream_options import CreateResponseBodyStreamOptions
    from .create_response_body_text import CreateResponseBodyText
    from .create_response_body_text_verbosity import CreateResponseBodyTextVerbosity
    from .create_response_body_tool_choice import CreateResponseBodyToolChoice
    from .create_response_body_truncation import CreateResponseBodyTruncation
    from .detail_enum import DetailEnum
    from .developer_message_item_param import DeveloperMessageItemParam
    from .developer_message_item_param_content import DeveloperMessageItemParamContent
    from .developer_message_item_param_role import DeveloperMessageItemParamRole
    from .developer_message_item_param_type import DeveloperMessageItemParamType
    from .empty_model_param import EmptyModelParam
    from .error import Error
    from .error_payload import ErrorPayload
    from .error_streaming_event import ErrorStreamingEvent
    from .error_streaming_event_error import ErrorStreamingEventError
    from .error_streaming_event_type import ErrorStreamingEventType
    from .function_call import FunctionCall
    from .function_call_item_param import FunctionCallItemParam
    from .function_call_item_param_status import FunctionCallItemParamStatus
    from .function_call_item_param_type import FunctionCallItemParamType
    from .function_call_item_status import FunctionCallItemStatus
    from .function_call_output import FunctionCallOutput
    from .function_call_output_item_param import FunctionCallOutputItemParam
    from .function_call_output_item_param_output import FunctionCallOutputItemParamOutput
    from .function_call_output_item_param_output_one_item import (
        FunctionCallOutputItemParamOutputOneItem,
        FunctionCallOutputItemParamOutputOneItem_InputFile,
        FunctionCallOutputItemParamOutputOneItem_InputImage,
        FunctionCallOutputItemParamOutputOneItem_InputText,
        FunctionCallOutputItemParamOutputOneItem_InputVideo,
    )
    from .function_call_output_item_param_status import FunctionCallOutputItemParamStatus
    from .function_call_output_item_param_type import FunctionCallOutputItemParamType
    from .function_call_output_output import FunctionCallOutputOutput
    from .function_call_output_output_one_item import (
        FunctionCallOutputOutputOneItem,
        FunctionCallOutputOutputOneItem_InputFile,
        FunctionCallOutputOutputOneItem_InputImage,
        FunctionCallOutputOutputOneItem_InputText,
    )
    from .function_call_output_status import FunctionCallOutputStatus
    from .function_call_output_status_enum import FunctionCallOutputStatusEnum
    from .function_call_status import FunctionCallStatus
    from .function_tool import FunctionTool
    from .function_tool_choice import FunctionToolChoice
    from .function_tool_choice_type import FunctionToolChoiceType
    from .function_tool_param import FunctionToolParam
    from .function_tool_param_type import FunctionToolParamType
    from .function_tool_type import FunctionToolType
    from .image_detail import ImageDetail
    from .include_enum import IncludeEnum
    from .incomplete_details import IncompleteDetails
    from .input_file_content import InputFileContent
    from .input_file_content_param import InputFileContentParam
    from .input_image_content import InputImageContent
    from .input_image_content_detail import InputImageContentDetail
    from .input_image_content_param_auto_param import InputImageContentParamAutoParam
    from .input_image_content_param_auto_param_detail import InputImageContentParamAutoParamDetail
    from .input_text_content import InputTextContent
    from .input_text_content_param import InputTextContentParam
    from .input_text_content_param_type import InputTextContentParamType
    from .input_tokens_details import InputTokensDetails
    from .input_video_content import InputVideoContent
    from .item_field import (
        ItemField,
        ItemField_FunctionCall,
        ItemField_FunctionCallOutput,
        ItemField_Message,
        ItemField_Reasoning,
    )
    from .item_param import ItemParam
    from .item_reference_param import ItemReferenceParam
    from .item_reference_param_type import ItemReferenceParamType
    from .json_object_response_format import JsonObjectResponseFormat
    from .json_schema_response_format import JsonSchemaResponseFormat
    from .json_schema_response_format_param import JsonSchemaResponseFormatParam
    from .log_prob import LogProb
    from .message import Message
    from .message_content_item import (
        MessageContentItem,
        MessageContentItem_InputFile,
        MessageContentItem_InputImage,
        MessageContentItem_InputText,
        MessageContentItem_InputVideo,
        MessageContentItem_OutputText,
        MessageContentItem_ReasoningText,
        MessageContentItem_Refusal,
        MessageContentItem_SummaryText,
        MessageContentItem_Text,
    )
    from .message_role import MessageRole
    from .message_status import MessageStatus
    from .metadata_param import MetadataParam
    from .output_text_content import OutputTextContent
    from .output_text_content_param import OutputTextContentParam
    from .output_tokens_details import OutputTokensDetails
    from .reasoning import Reasoning
    from .reasoning_body import ReasoningBody
    from .reasoning_body_content_item import (
        ReasoningBodyContentItem,
        ReasoningBodyContentItem_InputFile,
        ReasoningBodyContentItem_InputImage,
        ReasoningBodyContentItem_InputText,
        ReasoningBodyContentItem_OutputText,
        ReasoningBodyContentItem_ReasoningText,
        ReasoningBodyContentItem_Refusal,
        ReasoningBodyContentItem_SummaryText,
        ReasoningBodyContentItem_Text,
    )
    from .reasoning_body_summary_item import (
        ReasoningBodySummaryItem,
        ReasoningBodySummaryItem_InputFile,
        ReasoningBodySummaryItem_InputImage,
        ReasoningBodySummaryItem_InputText,
        ReasoningBodySummaryItem_OutputText,
        ReasoningBodySummaryItem_ReasoningText,
        ReasoningBodySummaryItem_Refusal,
        ReasoningBodySummaryItem_SummaryText,
        ReasoningBodySummaryItem_Text,
    )
    from .reasoning_effort_enum import ReasoningEffortEnum
    from .reasoning_item_param import ReasoningItemParam
    from .reasoning_item_param_type import ReasoningItemParamType
    from .reasoning_param import ReasoningParam
    from .reasoning_param_summary import ReasoningParamSummary
    from .reasoning_summary import ReasoningSummary
    from .reasoning_summary_content_param import ReasoningSummaryContentParam
    from .reasoning_summary_content_param_type import ReasoningSummaryContentParamType
    from .reasoning_summary_enum import ReasoningSummaryEnum
    from .reasoning_text_content import ReasoningTextContent
    from .refusal_content import RefusalContent
    from .refusal_content_param import RefusalContentParam
    from .response_completed_streaming_event import ResponseCompletedStreamingEvent
    from .response_completed_streaming_event_response import ResponseCompletedStreamingEventResponse
    from .response_completed_streaming_event_response_error import ResponseCompletedStreamingEventResponseError
    from .response_completed_streaming_event_response_incomplete_details import (
        ResponseCompletedStreamingEventResponseIncompleteDetails,
    )
    from .response_completed_streaming_event_response_object import ResponseCompletedStreamingEventResponseObject
    from .response_completed_streaming_event_response_reasoning import ResponseCompletedStreamingEventResponseReasoning
    from .response_completed_streaming_event_response_reasoning_summary import (
        ResponseCompletedStreamingEventResponseReasoningSummary,
    )
    from .response_completed_streaming_event_response_text import ResponseCompletedStreamingEventResponseText
    from .response_completed_streaming_event_response_text_format import (
        ResponseCompletedStreamingEventResponseTextFormat,
        ResponseCompletedStreamingEventResponseTextFormat_JsonObject,
        ResponseCompletedStreamingEventResponseTextFormat_JsonSchema,
        ResponseCompletedStreamingEventResponseTextFormat_Text,
    )
    from .response_completed_streaming_event_response_tool_choice import (
        ResponseCompletedStreamingEventResponseToolChoice,
    )
    from .response_completed_streaming_event_response_truncation import (
        ResponseCompletedStreamingEventResponseTruncation,
    )
    from .response_completed_streaming_event_response_usage import ResponseCompletedStreamingEventResponseUsage
    from .response_completed_streaming_event_response_usage_input_tokens_details import (
        ResponseCompletedStreamingEventResponseUsageInputTokensDetails,
    )
    from .response_completed_streaming_event_response_usage_output_tokens_details import (
        ResponseCompletedStreamingEventResponseUsageOutputTokensDetails,
    )
    from .response_completed_streaming_event_type import ResponseCompletedStreamingEventType
    from .response_content_part_added_streaming_event import ResponseContentPartAddedStreamingEvent
    from .response_content_part_added_streaming_event_part import (
        ResponseContentPartAddedStreamingEventPart,
        ResponseContentPartAddedStreamingEventPart_InputFile,
        ResponseContentPartAddedStreamingEventPart_InputImage,
        ResponseContentPartAddedStreamingEventPart_InputText,
        ResponseContentPartAddedStreamingEventPart_OutputText,
        ResponseContentPartAddedStreamingEventPart_ReasoningText,
        ResponseContentPartAddedStreamingEventPart_Refusal,
        ResponseContentPartAddedStreamingEventPart_SummaryText,
        ResponseContentPartAddedStreamingEventPart_Text,
    )
    from .response_content_part_added_streaming_event_type import ResponseContentPartAddedStreamingEventType
    from .response_content_part_done_streaming_event import ResponseContentPartDoneStreamingEvent
    from .response_content_part_done_streaming_event_part import (
        ResponseContentPartDoneStreamingEventPart,
        ResponseContentPartDoneStreamingEventPart_InputFile,
        ResponseContentPartDoneStreamingEventPart_InputImage,
        ResponseContentPartDoneStreamingEventPart_InputText,
        ResponseContentPartDoneStreamingEventPart_OutputText,
        ResponseContentPartDoneStreamingEventPart_ReasoningText,
        ResponseContentPartDoneStreamingEventPart_Refusal,
        ResponseContentPartDoneStreamingEventPart_SummaryText,
        ResponseContentPartDoneStreamingEventPart_Text,
    )
    from .response_content_part_done_streaming_event_type import ResponseContentPartDoneStreamingEventType
    from .response_created_streaming_event import ResponseCreatedStreamingEvent
    from .response_created_streaming_event_response import ResponseCreatedStreamingEventResponse
    from .response_created_streaming_event_response_error import ResponseCreatedStreamingEventResponseError
    from .response_created_streaming_event_response_incomplete_details import (
        ResponseCreatedStreamingEventResponseIncompleteDetails,
    )
    from .response_created_streaming_event_response_object import ResponseCreatedStreamingEventResponseObject
    from .response_created_streaming_event_response_reasoning import ResponseCreatedStreamingEventResponseReasoning
    from .response_created_streaming_event_response_reasoning_summary import (
        ResponseCreatedStreamingEventResponseReasoningSummary,
    )
    from .response_created_streaming_event_response_text import ResponseCreatedStreamingEventResponseText
    from .response_created_streaming_event_response_text_format import (
        ResponseCreatedStreamingEventResponseTextFormat,
        ResponseCreatedStreamingEventResponseTextFormat_JsonObject,
        ResponseCreatedStreamingEventResponseTextFormat_JsonSchema,
        ResponseCreatedStreamingEventResponseTextFormat_Text,
    )
    from .response_created_streaming_event_response_tool_choice import ResponseCreatedStreamingEventResponseToolChoice
    from .response_created_streaming_event_response_truncation import ResponseCreatedStreamingEventResponseTruncation
    from .response_created_streaming_event_response_usage import ResponseCreatedStreamingEventResponseUsage
    from .response_created_streaming_event_response_usage_input_tokens_details import (
        ResponseCreatedStreamingEventResponseUsageInputTokensDetails,
    )
    from .response_created_streaming_event_response_usage_output_tokens_details import (
        ResponseCreatedStreamingEventResponseUsageOutputTokensDetails,
    )
    from .response_created_streaming_event_type import ResponseCreatedStreamingEventType
    from .response_failed_streaming_event import ResponseFailedStreamingEvent
    from .response_failed_streaming_event_response import ResponseFailedStreamingEventResponse
    from .response_failed_streaming_event_response_error import ResponseFailedStreamingEventResponseError
    from .response_failed_streaming_event_response_incomplete_details import (
        ResponseFailedStreamingEventResponseIncompleteDetails,
    )
    from .response_failed_streaming_event_response_object import ResponseFailedStreamingEventResponseObject
    from .response_failed_streaming_event_response_reasoning import ResponseFailedStreamingEventResponseReasoning
    from .response_failed_streaming_event_response_reasoning_summary import (
        ResponseFailedStreamingEventResponseReasoningSummary,
    )
    from .response_failed_streaming_event_response_text import ResponseFailedStreamingEventResponseText
    from .response_failed_streaming_event_response_text_format import (
        ResponseFailedStreamingEventResponseTextFormat,
        ResponseFailedStreamingEventResponseTextFormat_JsonObject,
        ResponseFailedStreamingEventResponseTextFormat_JsonSchema,
        ResponseFailedStreamingEventResponseTextFormat_Text,
    )
    from .response_failed_streaming_event_response_tool_choice import ResponseFailedStreamingEventResponseToolChoice
    from .response_failed_streaming_event_response_truncation import ResponseFailedStreamingEventResponseTruncation
    from .response_failed_streaming_event_response_usage import ResponseFailedStreamingEventResponseUsage
    from .response_failed_streaming_event_response_usage_input_tokens_details import (
        ResponseFailedStreamingEventResponseUsageInputTokensDetails,
    )
    from .response_failed_streaming_event_response_usage_output_tokens_details import (
        ResponseFailedStreamingEventResponseUsageOutputTokensDetails,
    )
    from .response_failed_streaming_event_type import ResponseFailedStreamingEventType
    from .response_function_call_arguments_delta_streaming_event import ResponseFunctionCallArgumentsDeltaStreamingEvent
    from .response_function_call_arguments_delta_streaming_event_type import (
        ResponseFunctionCallArgumentsDeltaStreamingEventType,
    )
    from .response_function_call_arguments_done_streaming_event import ResponseFunctionCallArgumentsDoneStreamingEvent
    from .response_function_call_arguments_done_streaming_event_type import (
        ResponseFunctionCallArgumentsDoneStreamingEventType,
    )
    from .response_in_progress_streaming_event import ResponseInProgressStreamingEvent
    from .response_in_progress_streaming_event_response import ResponseInProgressStreamingEventResponse
    from .response_in_progress_streaming_event_response_error import ResponseInProgressStreamingEventResponseError
    from .response_in_progress_streaming_event_response_incomplete_details import (
        ResponseInProgressStreamingEventResponseIncompleteDetails,
    )
    from .response_in_progress_streaming_event_response_object import ResponseInProgressStreamingEventResponseObject
    from .response_in_progress_streaming_event_response_reasoning import (
        ResponseInProgressStreamingEventResponseReasoning,
    )
    from .response_in_progress_streaming_event_response_reasoning_summary import (
        ResponseInProgressStreamingEventResponseReasoningSummary,
    )
    from .response_in_progress_streaming_event_response_text import ResponseInProgressStreamingEventResponseText
    from .response_in_progress_streaming_event_response_text_format import (
        ResponseInProgressStreamingEventResponseTextFormat,
        ResponseInProgressStreamingEventResponseTextFormat_JsonObject,
        ResponseInProgressStreamingEventResponseTextFormat_JsonSchema,
        ResponseInProgressStreamingEventResponseTextFormat_Text,
    )
    from .response_in_progress_streaming_event_response_tool_choice import (
        ResponseInProgressStreamingEventResponseToolChoice,
    )
    from .response_in_progress_streaming_event_response_truncation import (
        ResponseInProgressStreamingEventResponseTruncation,
    )
    from .response_in_progress_streaming_event_response_usage import ResponseInProgressStreamingEventResponseUsage
    from .response_in_progress_streaming_event_response_usage_input_tokens_details import (
        ResponseInProgressStreamingEventResponseUsageInputTokensDetails,
    )
    from .response_in_progress_streaming_event_response_usage_output_tokens_details import (
        ResponseInProgressStreamingEventResponseUsageOutputTokensDetails,
    )
    from .response_in_progress_streaming_event_type import ResponseInProgressStreamingEventType
    from .response_incomplete_streaming_event import ResponseIncompleteStreamingEvent
    from .response_incomplete_streaming_event_response import ResponseIncompleteStreamingEventResponse
    from .response_incomplete_streaming_event_response_error import ResponseIncompleteStreamingEventResponseError
    from .response_incomplete_streaming_event_response_incomplete_details import (
        ResponseIncompleteStreamingEventResponseIncompleteDetails,
    )
    from .response_incomplete_streaming_event_response_object import ResponseIncompleteStreamingEventResponseObject
    from .response_incomplete_streaming_event_response_reasoning import (
        ResponseIncompleteStreamingEventResponseReasoning,
    )
    from .response_incomplete_streaming_event_response_reasoning_summary import (
        ResponseIncompleteStreamingEventResponseReasoningSummary,
    )
    from .response_incomplete_streaming_event_response_text import ResponseIncompleteStreamingEventResponseText
    from .response_incomplete_streaming_event_response_text_format import (
        ResponseIncompleteStreamingEventResponseTextFormat,
        ResponseIncompleteStreamingEventResponseTextFormat_JsonObject,
        ResponseIncompleteStreamingEventResponseTextFormat_JsonSchema,
        ResponseIncompleteStreamingEventResponseTextFormat_Text,
    )
    from .response_incomplete_streaming_event_response_tool_choice import (
        ResponseIncompleteStreamingEventResponseToolChoice,
    )
    from .response_incomplete_streaming_event_response_truncation import (
        ResponseIncompleteStreamingEventResponseTruncation,
    )
    from .response_incomplete_streaming_event_response_usage import ResponseIncompleteStreamingEventResponseUsage
    from .response_incomplete_streaming_event_response_usage_input_tokens_details import (
        ResponseIncompleteStreamingEventResponseUsageInputTokensDetails,
    )
    from .response_incomplete_streaming_event_response_usage_output_tokens_details import (
        ResponseIncompleteStreamingEventResponseUsageOutputTokensDetails,
    )
    from .response_incomplete_streaming_event_type import ResponseIncompleteStreamingEventType
    from .response_output_item_added_streaming_event import ResponseOutputItemAddedStreamingEvent
    from .response_output_item_added_streaming_event_item import (
        ResponseOutputItemAddedStreamingEventItem,
        ResponseOutputItemAddedStreamingEventItem_FunctionCall,
        ResponseOutputItemAddedStreamingEventItem_FunctionCallOutput,
        ResponseOutputItemAddedStreamingEventItem_Message,
        ResponseOutputItemAddedStreamingEventItem_Reasoning,
    )
    from .response_output_item_added_streaming_event_type import ResponseOutputItemAddedStreamingEventType
    from .response_output_item_done_streaming_event import ResponseOutputItemDoneStreamingEvent
    from .response_output_item_done_streaming_event_item import (
        ResponseOutputItemDoneStreamingEventItem,
        ResponseOutputItemDoneStreamingEventItem_FunctionCall,
        ResponseOutputItemDoneStreamingEventItem_FunctionCallOutput,
        ResponseOutputItemDoneStreamingEventItem_Message,
        ResponseOutputItemDoneStreamingEventItem_Reasoning,
    )
    from .response_output_item_done_streaming_event_type import ResponseOutputItemDoneStreamingEventType
    from .response_output_text_annotation_added_streaming_event import ResponseOutputTextAnnotationAddedStreamingEvent
    from .response_output_text_annotation_added_streaming_event_type import (
        ResponseOutputTextAnnotationAddedStreamingEventType,
    )
    from .response_output_text_delta_streaming_event import ResponseOutputTextDeltaStreamingEvent
    from .response_output_text_delta_streaming_event_type import ResponseOutputTextDeltaStreamingEventType
    from .response_output_text_done_streaming_event import ResponseOutputTextDoneStreamingEvent
    from .response_output_text_done_streaming_event_type import ResponseOutputTextDoneStreamingEventType
    from .response_queued_streaming_event import ResponseQueuedStreamingEvent
    from .response_queued_streaming_event_response import ResponseQueuedStreamingEventResponse
    from .response_queued_streaming_event_response_error import ResponseQueuedStreamingEventResponseError
    from .response_queued_streaming_event_response_incomplete_details import (
        ResponseQueuedStreamingEventResponseIncompleteDetails,
    )
    from .response_queued_streaming_event_response_object import ResponseQueuedStreamingEventResponseObject
    from .response_queued_streaming_event_response_reasoning import ResponseQueuedStreamingEventResponseReasoning
    from .response_queued_streaming_event_response_reasoning_summary import (
        ResponseQueuedStreamingEventResponseReasoningSummary,
    )
    from .response_queued_streaming_event_response_text import ResponseQueuedStreamingEventResponseText
    from .response_queued_streaming_event_response_text_format import (
        ResponseQueuedStreamingEventResponseTextFormat,
        ResponseQueuedStreamingEventResponseTextFormat_JsonObject,
        ResponseQueuedStreamingEventResponseTextFormat_JsonSchema,
        ResponseQueuedStreamingEventResponseTextFormat_Text,
    )
    from .response_queued_streaming_event_response_tool_choice import ResponseQueuedStreamingEventResponseToolChoice
    from .response_queued_streaming_event_response_truncation import ResponseQueuedStreamingEventResponseTruncation
    from .response_queued_streaming_event_response_usage import ResponseQueuedStreamingEventResponseUsage
    from .response_queued_streaming_event_response_usage_input_tokens_details import (
        ResponseQueuedStreamingEventResponseUsageInputTokensDetails,
    )
    from .response_queued_streaming_event_response_usage_output_tokens_details import (
        ResponseQueuedStreamingEventResponseUsageOutputTokensDetails,
    )
    from .response_queued_streaming_event_type import ResponseQueuedStreamingEventType
    from .response_reasoning_delta_streaming_event import ResponseReasoningDeltaStreamingEvent
    from .response_reasoning_delta_streaming_event_type import ResponseReasoningDeltaStreamingEventType
    from .response_reasoning_done_streaming_event import ResponseReasoningDoneStreamingEvent
    from .response_reasoning_done_streaming_event_type import ResponseReasoningDoneStreamingEventType
    from .response_reasoning_summary_delta_streaming_event import ResponseReasoningSummaryDeltaStreamingEvent
    from .response_reasoning_summary_delta_streaming_event_type import ResponseReasoningSummaryDeltaStreamingEventType
    from .response_reasoning_summary_done_streaming_event import ResponseReasoningSummaryDoneStreamingEvent
    from .response_reasoning_summary_done_streaming_event_type import ResponseReasoningSummaryDoneStreamingEventType
    from .response_reasoning_summary_part_added_streaming_event import ResponseReasoningSummaryPartAddedStreamingEvent
    from .response_reasoning_summary_part_added_streaming_event_part import (
        ResponseReasoningSummaryPartAddedStreamingEventPart,
        ResponseReasoningSummaryPartAddedStreamingEventPart_InputFile,
        ResponseReasoningSummaryPartAddedStreamingEventPart_InputImage,
        ResponseReasoningSummaryPartAddedStreamingEventPart_InputText,
        ResponseReasoningSummaryPartAddedStreamingEventPart_OutputText,
        ResponseReasoningSummaryPartAddedStreamingEventPart_ReasoningText,
        ResponseReasoningSummaryPartAddedStreamingEventPart_Refusal,
        ResponseReasoningSummaryPartAddedStreamingEventPart_SummaryText,
        ResponseReasoningSummaryPartAddedStreamingEventPart_Text,
    )
    from .response_reasoning_summary_part_added_streaming_event_type import (
        ResponseReasoningSummaryPartAddedStreamingEventType,
    )
    from .response_reasoning_summary_part_done_streaming_event import ResponseReasoningSummaryPartDoneStreamingEvent
    from .response_reasoning_summary_part_done_streaming_event_part import (
        ResponseReasoningSummaryPartDoneStreamingEventPart,
        ResponseReasoningSummaryPartDoneStreamingEventPart_InputFile,
        ResponseReasoningSummaryPartDoneStreamingEventPart_InputImage,
        ResponseReasoningSummaryPartDoneStreamingEventPart_InputText,
        ResponseReasoningSummaryPartDoneStreamingEventPart_OutputText,
        ResponseReasoningSummaryPartDoneStreamingEventPart_ReasoningText,
        ResponseReasoningSummaryPartDoneStreamingEventPart_Refusal,
        ResponseReasoningSummaryPartDoneStreamingEventPart_SummaryText,
        ResponseReasoningSummaryPartDoneStreamingEventPart_Text,
    )
    from .response_reasoning_summary_part_done_streaming_event_type import (
        ResponseReasoningSummaryPartDoneStreamingEventType,
    )
    from .response_refusal_delta_streaming_event import ResponseRefusalDeltaStreamingEvent
    from .response_refusal_delta_streaming_event_type import ResponseRefusalDeltaStreamingEventType
    from .response_refusal_done_streaming_event import ResponseRefusalDoneStreamingEvent
    from .response_refusal_done_streaming_event_type import ResponseRefusalDoneStreamingEventType
    from .response_resource import ResponseResource
    from .response_resource_error import ResponseResourceError
    from .response_resource_incomplete_details import ResponseResourceIncompleteDetails
    from .response_resource_object import ResponseResourceObject
    from .response_resource_reasoning import ResponseResourceReasoning
    from .response_resource_reasoning_summary import ResponseResourceReasoningSummary
    from .response_resource_text import ResponseResourceText
    from .response_resource_text_format import (
        ResponseResourceTextFormat,
        ResponseResourceTextFormat_JsonObject,
        ResponseResourceTextFormat_JsonSchema,
        ResponseResourceTextFormat_Text,
    )
    from .response_resource_tool_choice import ResponseResourceToolChoice
    from .response_resource_truncation import ResponseResourceTruncation
    from .response_resource_usage import ResponseResourceUsage
    from .response_resource_usage_input_tokens_details import ResponseResourceUsageInputTokensDetails
    from .response_resource_usage_output_tokens_details import ResponseResourceUsageOutputTokensDetails
    from .responses_tool_param import ResponsesToolParam
    from .service_tier_enum import ServiceTierEnum
    from .specific_function_param import SpecificFunctionParam
    from .specific_function_param_type import SpecificFunctionParamType
    from .specific_tool_choice_param import SpecificToolChoiceParam
    from .stream_options_param import StreamOptionsParam
    from .summary_text_content import SummaryTextContent
    from .system_message_item_param import SystemMessageItemParam
    from .system_message_item_param_content import SystemMessageItemParamContent
    from .system_message_item_param_role import SystemMessageItemParamRole
    from .system_message_item_param_type import SystemMessageItemParamType
    from .text_content import TextContent
    from .text_field import TextField
    from .text_field_format import (
        TextFieldFormat,
        TextFieldFormat_JsonObject,
        TextFieldFormat_JsonSchema,
        TextFieldFormat_Text,
    )
    from .text_format_param import TextFormatParam, TextFormatParam_JsonSchema, TextFormatParam_Text
    from .text_param import TextParam
    from .text_param_verbosity import TextParamVerbosity
    from .text_response_format import TextResponseFormat
    from .tool import Tool
    from .tool_choice_param import ToolChoiceParam
    from .tool_choice_value_enum import ToolChoiceValueEnum
    from .top_log_prob import TopLogProb
    from .truncation_enum import TruncationEnum
    from .url_citation_body import UrlCitationBody
    from .url_citation_body_type import UrlCitationBodyType
    from .url_citation_param import UrlCitationParam
    from .url_citation_param_type import UrlCitationParamType
    from .usage import Usage
    from .usage_input_tokens_details import UsageInputTokensDetails
    from .usage_output_tokens_details import UsageOutputTokensDetails
    from .user_message_item_param import UserMessageItemParam
    from .user_message_item_param_content import UserMessageItemParamContent
    from .user_message_item_param_content_zero_item import (
        UserMessageItemParamContentZeroItem,
        UserMessageItemParamContentZeroItem_InputFile,
        UserMessageItemParamContentZeroItem_InputImage,
        UserMessageItemParamContentZeroItem_InputText,
    )
    from .user_message_item_param_role import UserMessageItemParamRole
    from .user_message_item_param_type import UserMessageItemParamType
    from .verbosity_enum import VerbosityEnum
_dynamic_imports: typing.Dict[str, str] = {
    "AllowedToolChoice": ".allowed_tool_choice",
    "AllowedToolChoiceType": ".allowed_tool_choice_type",
    "AllowedToolsParam": ".allowed_tools_param",
    "AllowedToolsParamMode": ".allowed_tools_param_mode",
    "AllowedToolsParamType": ".allowed_tools_param_type",
    "Annotation": ".annotation",
    "AssistantMessageItemParam": ".assistant_message_item_param",
    "AssistantMessageItemParamContent": ".assistant_message_item_param_content",
    "AssistantMessageItemParamContentZeroItem": ".assistant_message_item_param_content_zero_item",
    "AssistantMessageItemParamContentZeroItem_OutputText": ".assistant_message_item_param_content_zero_item",
    "AssistantMessageItemParamContentZeroItem_Refusal": ".assistant_message_item_param_content_zero_item",
    "AssistantMessageItemParamRole": ".assistant_message_item_param_role",
    "AssistantMessageItemParamType": ".assistant_message_item_param_type",
    "CreateResponseBodyInput": ".create_response_body_input",
    "CreateResponseBodyReasoning": ".create_response_body_reasoning",
    "CreateResponseBodyReasoningSummary": ".create_response_body_reasoning_summary",
    "CreateResponseBodyServiceTier": ".create_response_body_service_tier",
    "CreateResponseBodyStreamOptions": ".create_response_body_stream_options",
    "CreateResponseBodyText": ".create_response_body_text",
    "CreateResponseBodyTextVerbosity": ".create_response_body_text_verbosity",
    "CreateResponseBodyToolChoice": ".create_response_body_tool_choice",
    "CreateResponseBodyTruncation": ".create_response_body_truncation",
    "DetailEnum": ".detail_enum",
    "DeveloperMessageItemParam": ".developer_message_item_param",
    "DeveloperMessageItemParamContent": ".developer_message_item_param_content",
    "DeveloperMessageItemParamRole": ".developer_message_item_param_role",
    "DeveloperMessageItemParamType": ".developer_message_item_param_type",
    "EmptyModelParam": ".empty_model_param",
    "Error": ".error",
    "ErrorPayload": ".error_payload",
    "ErrorStreamingEvent": ".error_streaming_event",
    "ErrorStreamingEventError": ".error_streaming_event_error",
    "ErrorStreamingEventType": ".error_streaming_event_type",
    "FunctionCall": ".function_call",
    "FunctionCallItemParam": ".function_call_item_param",
    "FunctionCallItemParamStatus": ".function_call_item_param_status",
    "FunctionCallItemParamType": ".function_call_item_param_type",
    "FunctionCallItemStatus": ".function_call_item_status",
    "FunctionCallOutput": ".function_call_output",
    "FunctionCallOutputItemParam": ".function_call_output_item_param",
    "FunctionCallOutputItemParamOutput": ".function_call_output_item_param_output",
    "FunctionCallOutputItemParamOutputOneItem": ".function_call_output_item_param_output_one_item",
    "FunctionCallOutputItemParamOutputOneItem_InputFile": ".function_call_output_item_param_output_one_item",
    "FunctionCallOutputItemParamOutputOneItem_InputImage": ".function_call_output_item_param_output_one_item",
    "FunctionCallOutputItemParamOutputOneItem_InputText": ".function_call_output_item_param_output_one_item",
    "FunctionCallOutputItemParamOutputOneItem_InputVideo": ".function_call_output_item_param_output_one_item",
    "FunctionCallOutputItemParamStatus": ".function_call_output_item_param_status",
    "FunctionCallOutputItemParamType": ".function_call_output_item_param_type",
    "FunctionCallOutputOutput": ".function_call_output_output",
    "FunctionCallOutputOutputOneItem": ".function_call_output_output_one_item",
    "FunctionCallOutputOutputOneItem_InputFile": ".function_call_output_output_one_item",
    "FunctionCallOutputOutputOneItem_InputImage": ".function_call_output_output_one_item",
    "FunctionCallOutputOutputOneItem_InputText": ".function_call_output_output_one_item",
    "FunctionCallOutputStatus": ".function_call_output_status",
    "FunctionCallOutputStatusEnum": ".function_call_output_status_enum",
    "FunctionCallStatus": ".function_call_status",
    "FunctionTool": ".function_tool",
    "FunctionToolChoice": ".function_tool_choice",
    "FunctionToolChoiceType": ".function_tool_choice_type",
    "FunctionToolParam": ".function_tool_param",
    "FunctionToolParamType": ".function_tool_param_type",
    "FunctionToolType": ".function_tool_type",
    "ImageDetail": ".image_detail",
    "IncludeEnum": ".include_enum",
    "IncompleteDetails": ".incomplete_details",
    "InputFileContent": ".input_file_content",
    "InputFileContentParam": ".input_file_content_param",
    "InputImageContent": ".input_image_content",
    "InputImageContentDetail": ".input_image_content_detail",
    "InputImageContentParamAutoParam": ".input_image_content_param_auto_param",
    "InputImageContentParamAutoParamDetail": ".input_image_content_param_auto_param_detail",
    "InputTextContent": ".input_text_content",
    "InputTextContentParam": ".input_text_content_param",
    "InputTextContentParamType": ".input_text_content_param_type",
    "InputTokensDetails": ".input_tokens_details",
    "InputVideoContent": ".input_video_content",
    "ItemField": ".item_field",
    "ItemField_FunctionCall": ".item_field",
    "ItemField_FunctionCallOutput": ".item_field",
    "ItemField_Message": ".item_field",
    "ItemField_Reasoning": ".item_field",
    "ItemParam": ".item_param",
    "ItemReferenceParam": ".item_reference_param",
    "ItemReferenceParamType": ".item_reference_param_type",
    "JsonObjectResponseFormat": ".json_object_response_format",
    "JsonSchemaResponseFormat": ".json_schema_response_format",
    "JsonSchemaResponseFormatParam": ".json_schema_response_format_param",
    "LogProb": ".log_prob",
    "Message": ".message",
    "MessageContentItem": ".message_content_item",
    "MessageContentItem_InputFile": ".message_content_item",
    "MessageContentItem_InputImage": ".message_content_item",
    "MessageContentItem_InputText": ".message_content_item",
    "MessageContentItem_InputVideo": ".message_content_item",
    "MessageContentItem_OutputText": ".message_content_item",
    "MessageContentItem_ReasoningText": ".message_content_item",
    "MessageContentItem_Refusal": ".message_content_item",
    "MessageContentItem_SummaryText": ".message_content_item",
    "MessageContentItem_Text": ".message_content_item",
    "MessageRole": ".message_role",
    "MessageStatus": ".message_status",
    "MetadataParam": ".metadata_param",
    "OutputTextContent": ".output_text_content",
    "OutputTextContentParam": ".output_text_content_param",
    "OutputTokensDetails": ".output_tokens_details",
    "Reasoning": ".reasoning",
    "ReasoningBody": ".reasoning_body",
    "ReasoningBodyContentItem": ".reasoning_body_content_item",
    "ReasoningBodyContentItem_InputFile": ".reasoning_body_content_item",
    "ReasoningBodyContentItem_InputImage": ".reasoning_body_content_item",
    "ReasoningBodyContentItem_InputText": ".reasoning_body_content_item",
    "ReasoningBodyContentItem_OutputText": ".reasoning_body_content_item",
    "ReasoningBodyContentItem_ReasoningText": ".reasoning_body_content_item",
    "ReasoningBodyContentItem_Refusal": ".reasoning_body_content_item",
    "ReasoningBodyContentItem_SummaryText": ".reasoning_body_content_item",
    "ReasoningBodyContentItem_Text": ".reasoning_body_content_item",
    "ReasoningBodySummaryItem": ".reasoning_body_summary_item",
    "ReasoningBodySummaryItem_InputFile": ".reasoning_body_summary_item",
    "ReasoningBodySummaryItem_InputImage": ".reasoning_body_summary_item",
    "ReasoningBodySummaryItem_InputText": ".reasoning_body_summary_item",
    "ReasoningBodySummaryItem_OutputText": ".reasoning_body_summary_item",
    "ReasoningBodySummaryItem_ReasoningText": ".reasoning_body_summary_item",
    "ReasoningBodySummaryItem_Refusal": ".reasoning_body_summary_item",
    "ReasoningBodySummaryItem_SummaryText": ".reasoning_body_summary_item",
    "ReasoningBodySummaryItem_Text": ".reasoning_body_summary_item",
    "ReasoningEffortEnum": ".reasoning_effort_enum",
    "ReasoningItemParam": ".reasoning_item_param",
    "ReasoningItemParamType": ".reasoning_item_param_type",
    "ReasoningParam": ".reasoning_param",
    "ReasoningParamSummary": ".reasoning_param_summary",
    "ReasoningSummary": ".reasoning_summary",
    "ReasoningSummaryContentParam": ".reasoning_summary_content_param",
    "ReasoningSummaryContentParamType": ".reasoning_summary_content_param_type",
    "ReasoningSummaryEnum": ".reasoning_summary_enum",
    "ReasoningTextContent": ".reasoning_text_content",
    "RefusalContent": ".refusal_content",
    "RefusalContentParam": ".refusal_content_param",
    "ResponseCompletedStreamingEvent": ".response_completed_streaming_event",
    "ResponseCompletedStreamingEventResponse": ".response_completed_streaming_event_response",
    "ResponseCompletedStreamingEventResponseError": ".response_completed_streaming_event_response_error",
    "ResponseCompletedStreamingEventResponseIncompleteDetails": ".response_completed_streaming_event_response_incomplete_details",
    "ResponseCompletedStreamingEventResponseObject": ".response_completed_streaming_event_response_object",
    "ResponseCompletedStreamingEventResponseReasoning": ".response_completed_streaming_event_response_reasoning",
    "ResponseCompletedStreamingEventResponseReasoningSummary": ".response_completed_streaming_event_response_reasoning_summary",
    "ResponseCompletedStreamingEventResponseText": ".response_completed_streaming_event_response_text",
    "ResponseCompletedStreamingEventResponseTextFormat": ".response_completed_streaming_event_response_text_format",
    "ResponseCompletedStreamingEventResponseTextFormat_JsonObject": ".response_completed_streaming_event_response_text_format",
    "ResponseCompletedStreamingEventResponseTextFormat_JsonSchema": ".response_completed_streaming_event_response_text_format",
    "ResponseCompletedStreamingEventResponseTextFormat_Text": ".response_completed_streaming_event_response_text_format",
    "ResponseCompletedStreamingEventResponseToolChoice": ".response_completed_streaming_event_response_tool_choice",
    "ResponseCompletedStreamingEventResponseTruncation": ".response_completed_streaming_event_response_truncation",
    "ResponseCompletedStreamingEventResponseUsage": ".response_completed_streaming_event_response_usage",
    "ResponseCompletedStreamingEventResponseUsageInputTokensDetails": ".response_completed_streaming_event_response_usage_input_tokens_details",
    "ResponseCompletedStreamingEventResponseUsageOutputTokensDetails": ".response_completed_streaming_event_response_usage_output_tokens_details",
    "ResponseCompletedStreamingEventType": ".response_completed_streaming_event_type",
    "ResponseContentPartAddedStreamingEvent": ".response_content_part_added_streaming_event",
    "ResponseContentPartAddedStreamingEventPart": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventPart_InputFile": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventPart_InputImage": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventPart_InputText": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventPart_OutputText": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventPart_ReasoningText": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventPart_Refusal": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventPart_SummaryText": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventPart_Text": ".response_content_part_added_streaming_event_part",
    "ResponseContentPartAddedStreamingEventType": ".response_content_part_added_streaming_event_type",
    "ResponseContentPartDoneStreamingEvent": ".response_content_part_done_streaming_event",
    "ResponseContentPartDoneStreamingEventPart": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventPart_InputFile": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventPart_InputImage": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventPart_InputText": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventPart_OutputText": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventPart_ReasoningText": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventPart_Refusal": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventPart_SummaryText": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventPart_Text": ".response_content_part_done_streaming_event_part",
    "ResponseContentPartDoneStreamingEventType": ".response_content_part_done_streaming_event_type",
    "ResponseCreatedStreamingEvent": ".response_created_streaming_event",
    "ResponseCreatedStreamingEventResponse": ".response_created_streaming_event_response",
    "ResponseCreatedStreamingEventResponseError": ".response_created_streaming_event_response_error",
    "ResponseCreatedStreamingEventResponseIncompleteDetails": ".response_created_streaming_event_response_incomplete_details",
    "ResponseCreatedStreamingEventResponseObject": ".response_created_streaming_event_response_object",
    "ResponseCreatedStreamingEventResponseReasoning": ".response_created_streaming_event_response_reasoning",
    "ResponseCreatedStreamingEventResponseReasoningSummary": ".response_created_streaming_event_response_reasoning_summary",
    "ResponseCreatedStreamingEventResponseText": ".response_created_streaming_event_response_text",
    "ResponseCreatedStreamingEventResponseTextFormat": ".response_created_streaming_event_response_text_format",
    "ResponseCreatedStreamingEventResponseTextFormat_JsonObject": ".response_created_streaming_event_response_text_format",
    "ResponseCreatedStreamingEventResponseTextFormat_JsonSchema": ".response_created_streaming_event_response_text_format",
    "ResponseCreatedStreamingEventResponseTextFormat_Text": ".response_created_streaming_event_response_text_format",
    "ResponseCreatedStreamingEventResponseToolChoice": ".response_created_streaming_event_response_tool_choice",
    "ResponseCreatedStreamingEventResponseTruncation": ".response_created_streaming_event_response_truncation",
    "ResponseCreatedStreamingEventResponseUsage": ".response_created_streaming_event_response_usage",
    "ResponseCreatedStreamingEventResponseUsageInputTokensDetails": ".response_created_streaming_event_response_usage_input_tokens_details",
    "ResponseCreatedStreamingEventResponseUsageOutputTokensDetails": ".response_created_streaming_event_response_usage_output_tokens_details",
    "ResponseCreatedStreamingEventType": ".response_created_streaming_event_type",
    "ResponseFailedStreamingEvent": ".response_failed_streaming_event",
    "ResponseFailedStreamingEventResponse": ".response_failed_streaming_event_response",
    "ResponseFailedStreamingEventResponseError": ".response_failed_streaming_event_response_error",
    "ResponseFailedStreamingEventResponseIncompleteDetails": ".response_failed_streaming_event_response_incomplete_details",
    "ResponseFailedStreamingEventResponseObject": ".response_failed_streaming_event_response_object",
    "ResponseFailedStreamingEventResponseReasoning": ".response_failed_streaming_event_response_reasoning",
    "ResponseFailedStreamingEventResponseReasoningSummary": ".response_failed_streaming_event_response_reasoning_summary",
    "ResponseFailedStreamingEventResponseText": ".response_failed_streaming_event_response_text",
    "ResponseFailedStreamingEventResponseTextFormat": ".response_failed_streaming_event_response_text_format",
    "ResponseFailedStreamingEventResponseTextFormat_JsonObject": ".response_failed_streaming_event_response_text_format",
    "ResponseFailedStreamingEventResponseTextFormat_JsonSchema": ".response_failed_streaming_event_response_text_format",
    "ResponseFailedStreamingEventResponseTextFormat_Text": ".response_failed_streaming_event_response_text_format",
    "ResponseFailedStreamingEventResponseToolChoice": ".response_failed_streaming_event_response_tool_choice",
    "ResponseFailedStreamingEventResponseTruncation": ".response_failed_streaming_event_response_truncation",
    "ResponseFailedStreamingEventResponseUsage": ".response_failed_streaming_event_response_usage",
    "ResponseFailedStreamingEventResponseUsageInputTokensDetails": ".response_failed_streaming_event_response_usage_input_tokens_details",
    "ResponseFailedStreamingEventResponseUsageOutputTokensDetails": ".response_failed_streaming_event_response_usage_output_tokens_details",
    "ResponseFailedStreamingEventType": ".response_failed_streaming_event_type",
    "ResponseFunctionCallArgumentsDeltaStreamingEvent": ".response_function_call_arguments_delta_streaming_event",
    "ResponseFunctionCallArgumentsDeltaStreamingEventType": ".response_function_call_arguments_delta_streaming_event_type",
    "ResponseFunctionCallArgumentsDoneStreamingEvent": ".response_function_call_arguments_done_streaming_event",
    "ResponseFunctionCallArgumentsDoneStreamingEventType": ".response_function_call_arguments_done_streaming_event_type",
    "ResponseInProgressStreamingEvent": ".response_in_progress_streaming_event",
    "ResponseInProgressStreamingEventResponse": ".response_in_progress_streaming_event_response",
    "ResponseInProgressStreamingEventResponseError": ".response_in_progress_streaming_event_response_error",
    "ResponseInProgressStreamingEventResponseIncompleteDetails": ".response_in_progress_streaming_event_response_incomplete_details",
    "ResponseInProgressStreamingEventResponseObject": ".response_in_progress_streaming_event_response_object",
    "ResponseInProgressStreamingEventResponseReasoning": ".response_in_progress_streaming_event_response_reasoning",
    "ResponseInProgressStreamingEventResponseReasoningSummary": ".response_in_progress_streaming_event_response_reasoning_summary",
    "ResponseInProgressStreamingEventResponseText": ".response_in_progress_streaming_event_response_text",
    "ResponseInProgressStreamingEventResponseTextFormat": ".response_in_progress_streaming_event_response_text_format",
    "ResponseInProgressStreamingEventResponseTextFormat_JsonObject": ".response_in_progress_streaming_event_response_text_format",
    "ResponseInProgressStreamingEventResponseTextFormat_JsonSchema": ".response_in_progress_streaming_event_response_text_format",
    "ResponseInProgressStreamingEventResponseTextFormat_Text": ".response_in_progress_streaming_event_response_text_format",
    "ResponseInProgressStreamingEventResponseToolChoice": ".response_in_progress_streaming_event_response_tool_choice",
    "ResponseInProgressStreamingEventResponseTruncation": ".response_in_progress_streaming_event_response_truncation",
    "ResponseInProgressStreamingEventResponseUsage": ".response_in_progress_streaming_event_response_usage",
    "ResponseInProgressStreamingEventResponseUsageInputTokensDetails": ".response_in_progress_streaming_event_response_usage_input_tokens_details",
    "ResponseInProgressStreamingEventResponseUsageOutputTokensDetails": ".response_in_progress_streaming_event_response_usage_output_tokens_details",
    "ResponseInProgressStreamingEventType": ".response_in_progress_streaming_event_type",
    "ResponseIncompleteStreamingEvent": ".response_incomplete_streaming_event",
    "ResponseIncompleteStreamingEventResponse": ".response_incomplete_streaming_event_response",
    "ResponseIncompleteStreamingEventResponseError": ".response_incomplete_streaming_event_response_error",
    "ResponseIncompleteStreamingEventResponseIncompleteDetails": ".response_incomplete_streaming_event_response_incomplete_details",
    "ResponseIncompleteStreamingEventResponseObject": ".response_incomplete_streaming_event_response_object",
    "ResponseIncompleteStreamingEventResponseReasoning": ".response_incomplete_streaming_event_response_reasoning",
    "ResponseIncompleteStreamingEventResponseReasoningSummary": ".response_incomplete_streaming_event_response_reasoning_summary",
    "ResponseIncompleteStreamingEventResponseText": ".response_incomplete_streaming_event_response_text",
    "ResponseIncompleteStreamingEventResponseTextFormat": ".response_incomplete_streaming_event_response_text_format",
    "ResponseIncompleteStreamingEventResponseTextFormat_JsonObject": ".response_incomplete_streaming_event_response_text_format",
    "ResponseIncompleteStreamingEventResponseTextFormat_JsonSchema": ".response_incomplete_streaming_event_response_text_format",
    "ResponseIncompleteStreamingEventResponseTextFormat_Text": ".response_incomplete_streaming_event_response_text_format",
    "ResponseIncompleteStreamingEventResponseToolChoice": ".response_incomplete_streaming_event_response_tool_choice",
    "ResponseIncompleteStreamingEventResponseTruncation": ".response_incomplete_streaming_event_response_truncation",
    "ResponseIncompleteStreamingEventResponseUsage": ".response_incomplete_streaming_event_response_usage",
    "ResponseIncompleteStreamingEventResponseUsageInputTokensDetails": ".response_incomplete_streaming_event_response_usage_input_tokens_details",
    "ResponseIncompleteStreamingEventResponseUsageOutputTokensDetails": ".response_incomplete_streaming_event_response_usage_output_tokens_details",
    "ResponseIncompleteStreamingEventType": ".response_incomplete_streaming_event_type",
    "ResponseOutputItemAddedStreamingEvent": ".response_output_item_added_streaming_event",
    "ResponseOutputItemAddedStreamingEventItem": ".response_output_item_added_streaming_event_item",
    "ResponseOutputItemAddedStreamingEventItem_FunctionCall": ".response_output_item_added_streaming_event_item",
    "ResponseOutputItemAddedStreamingEventItem_FunctionCallOutput": ".response_output_item_added_streaming_event_item",
    "ResponseOutputItemAddedStreamingEventItem_Message": ".response_output_item_added_streaming_event_item",
    "ResponseOutputItemAddedStreamingEventItem_Reasoning": ".response_output_item_added_streaming_event_item",
    "ResponseOutputItemAddedStreamingEventType": ".response_output_item_added_streaming_event_type",
    "ResponseOutputItemDoneStreamingEvent": ".response_output_item_done_streaming_event",
    "ResponseOutputItemDoneStreamingEventItem": ".response_output_item_done_streaming_event_item",
    "ResponseOutputItemDoneStreamingEventItem_FunctionCall": ".response_output_item_done_streaming_event_item",
    "ResponseOutputItemDoneStreamingEventItem_FunctionCallOutput": ".response_output_item_done_streaming_event_item",
    "ResponseOutputItemDoneStreamingEventItem_Message": ".response_output_item_done_streaming_event_item",
    "ResponseOutputItemDoneStreamingEventItem_Reasoning": ".response_output_item_done_streaming_event_item",
    "ResponseOutputItemDoneStreamingEventType": ".response_output_item_done_streaming_event_type",
    "ResponseOutputTextAnnotationAddedStreamingEvent": ".response_output_text_annotation_added_streaming_event",
    "ResponseOutputTextAnnotationAddedStreamingEventType": ".response_output_text_annotation_added_streaming_event_type",
    "ResponseOutputTextDeltaStreamingEvent": ".response_output_text_delta_streaming_event",
    "ResponseOutputTextDeltaStreamingEventType": ".response_output_text_delta_streaming_event_type",
    "ResponseOutputTextDoneStreamingEvent": ".response_output_text_done_streaming_event",
    "ResponseOutputTextDoneStreamingEventType": ".response_output_text_done_streaming_event_type",
    "ResponseQueuedStreamingEvent": ".response_queued_streaming_event",
    "ResponseQueuedStreamingEventResponse": ".response_queued_streaming_event_response",
    "ResponseQueuedStreamingEventResponseError": ".response_queued_streaming_event_response_error",
    "ResponseQueuedStreamingEventResponseIncompleteDetails": ".response_queued_streaming_event_response_incomplete_details",
    "ResponseQueuedStreamingEventResponseObject": ".response_queued_streaming_event_response_object",
    "ResponseQueuedStreamingEventResponseReasoning": ".response_queued_streaming_event_response_reasoning",
    "ResponseQueuedStreamingEventResponseReasoningSummary": ".response_queued_streaming_event_response_reasoning_summary",
    "ResponseQueuedStreamingEventResponseText": ".response_queued_streaming_event_response_text",
    "ResponseQueuedStreamingEventResponseTextFormat": ".response_queued_streaming_event_response_text_format",
    "ResponseQueuedStreamingEventResponseTextFormat_JsonObject": ".response_queued_streaming_event_response_text_format",
    "ResponseQueuedStreamingEventResponseTextFormat_JsonSchema": ".response_queued_streaming_event_response_text_format",
    "ResponseQueuedStreamingEventResponseTextFormat_Text": ".response_queued_streaming_event_response_text_format",
    "ResponseQueuedStreamingEventResponseToolChoice": ".response_queued_streaming_event_response_tool_choice",
    "ResponseQueuedStreamingEventResponseTruncation": ".response_queued_streaming_event_response_truncation",
    "ResponseQueuedStreamingEventResponseUsage": ".response_queued_streaming_event_response_usage",
    "ResponseQueuedStreamingEventResponseUsageInputTokensDetails": ".response_queued_streaming_event_response_usage_input_tokens_details",
    "ResponseQueuedStreamingEventResponseUsageOutputTokensDetails": ".response_queued_streaming_event_response_usage_output_tokens_details",
    "ResponseQueuedStreamingEventType": ".response_queued_streaming_event_type",
    "ResponseReasoningDeltaStreamingEvent": ".response_reasoning_delta_streaming_event",
    "ResponseReasoningDeltaStreamingEventType": ".response_reasoning_delta_streaming_event_type",
    "ResponseReasoningDoneStreamingEvent": ".response_reasoning_done_streaming_event",
    "ResponseReasoningDoneStreamingEventType": ".response_reasoning_done_streaming_event_type",
    "ResponseReasoningSummaryDeltaStreamingEvent": ".response_reasoning_summary_delta_streaming_event",
    "ResponseReasoningSummaryDeltaStreamingEventType": ".response_reasoning_summary_delta_streaming_event_type",
    "ResponseReasoningSummaryDoneStreamingEvent": ".response_reasoning_summary_done_streaming_event",
    "ResponseReasoningSummaryDoneStreamingEventType": ".response_reasoning_summary_done_streaming_event_type",
    "ResponseReasoningSummaryPartAddedStreamingEvent": ".response_reasoning_summary_part_added_streaming_event",
    "ResponseReasoningSummaryPartAddedStreamingEventPart": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_InputFile": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_InputImage": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_InputText": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_OutputText": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_ReasoningText": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_Refusal": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_SummaryText": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_Text": ".response_reasoning_summary_part_added_streaming_event_part",
    "ResponseReasoningSummaryPartAddedStreamingEventType": ".response_reasoning_summary_part_added_streaming_event_type",
    "ResponseReasoningSummaryPartDoneStreamingEvent": ".response_reasoning_summary_part_done_streaming_event",
    "ResponseReasoningSummaryPartDoneStreamingEventPart": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_InputFile": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_InputImage": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_InputText": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_OutputText": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_ReasoningText": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_Refusal": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_SummaryText": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_Text": ".response_reasoning_summary_part_done_streaming_event_part",
    "ResponseReasoningSummaryPartDoneStreamingEventType": ".response_reasoning_summary_part_done_streaming_event_type",
    "ResponseRefusalDeltaStreamingEvent": ".response_refusal_delta_streaming_event",
    "ResponseRefusalDeltaStreamingEventType": ".response_refusal_delta_streaming_event_type",
    "ResponseRefusalDoneStreamingEvent": ".response_refusal_done_streaming_event",
    "ResponseRefusalDoneStreamingEventType": ".response_refusal_done_streaming_event_type",
    "ResponseResource": ".response_resource",
    "ResponseResourceError": ".response_resource_error",
    "ResponseResourceIncompleteDetails": ".response_resource_incomplete_details",
    "ResponseResourceObject": ".response_resource_object",
    "ResponseResourceReasoning": ".response_resource_reasoning",
    "ResponseResourceReasoningSummary": ".response_resource_reasoning_summary",
    "ResponseResourceText": ".response_resource_text",
    "ResponseResourceTextFormat": ".response_resource_text_format",
    "ResponseResourceTextFormat_JsonObject": ".response_resource_text_format",
    "ResponseResourceTextFormat_JsonSchema": ".response_resource_text_format",
    "ResponseResourceTextFormat_Text": ".response_resource_text_format",
    "ResponseResourceToolChoice": ".response_resource_tool_choice",
    "ResponseResourceTruncation": ".response_resource_truncation",
    "ResponseResourceUsage": ".response_resource_usage",
    "ResponseResourceUsageInputTokensDetails": ".response_resource_usage_input_tokens_details",
    "ResponseResourceUsageOutputTokensDetails": ".response_resource_usage_output_tokens_details",
    "ResponsesToolParam": ".responses_tool_param",
    "ServiceTierEnum": ".service_tier_enum",
    "SpecificFunctionParam": ".specific_function_param",
    "SpecificFunctionParamType": ".specific_function_param_type",
    "SpecificToolChoiceParam": ".specific_tool_choice_param",
    "StreamOptionsParam": ".stream_options_param",
    "SummaryTextContent": ".summary_text_content",
    "SystemMessageItemParam": ".system_message_item_param",
    "SystemMessageItemParamContent": ".system_message_item_param_content",
    "SystemMessageItemParamRole": ".system_message_item_param_role",
    "SystemMessageItemParamType": ".system_message_item_param_type",
    "TextContent": ".text_content",
    "TextField": ".text_field",
    "TextFieldFormat": ".text_field_format",
    "TextFieldFormat_JsonObject": ".text_field_format",
    "TextFieldFormat_JsonSchema": ".text_field_format",
    "TextFieldFormat_Text": ".text_field_format",
    "TextFormatParam": ".text_format_param",
    "TextFormatParam_JsonSchema": ".text_format_param",
    "TextFormatParam_Text": ".text_format_param",
    "TextParam": ".text_param",
    "TextParamVerbosity": ".text_param_verbosity",
    "TextResponseFormat": ".text_response_format",
    "Tool": ".tool",
    "ToolChoiceParam": ".tool_choice_param",
    "ToolChoiceValueEnum": ".tool_choice_value_enum",
    "TopLogProb": ".top_log_prob",
    "TruncationEnum": ".truncation_enum",
    "UrlCitationBody": ".url_citation_body",
    "UrlCitationBodyType": ".url_citation_body_type",
    "UrlCitationParam": ".url_citation_param",
    "UrlCitationParamType": ".url_citation_param_type",
    "Usage": ".usage",
    "UsageInputTokensDetails": ".usage_input_tokens_details",
    "UsageOutputTokensDetails": ".usage_output_tokens_details",
    "UserMessageItemParam": ".user_message_item_param",
    "UserMessageItemParamContent": ".user_message_item_param_content",
    "UserMessageItemParamContentZeroItem": ".user_message_item_param_content_zero_item",
    "UserMessageItemParamContentZeroItem_InputFile": ".user_message_item_param_content_zero_item",
    "UserMessageItemParamContentZeroItem_InputImage": ".user_message_item_param_content_zero_item",
    "UserMessageItemParamContentZeroItem_InputText": ".user_message_item_param_content_zero_item",
    "UserMessageItemParamRole": ".user_message_item_param_role",
    "UserMessageItemParamType": ".user_message_item_param_type",
    "VerbosityEnum": ".verbosity_enum",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AllowedToolChoice",
    "AllowedToolChoiceType",
    "AllowedToolsParam",
    "AllowedToolsParamMode",
    "AllowedToolsParamType",
    "Annotation",
    "AssistantMessageItemParam",
    "AssistantMessageItemParamContent",
    "AssistantMessageItemParamContentZeroItem",
    "AssistantMessageItemParamContentZeroItem_OutputText",
    "AssistantMessageItemParamContentZeroItem_Refusal",
    "AssistantMessageItemParamRole",
    "AssistantMessageItemParamType",
    "CreateResponseBodyInput",
    "CreateResponseBodyReasoning",
    "CreateResponseBodyReasoningSummary",
    "CreateResponseBodyServiceTier",
    "CreateResponseBodyStreamOptions",
    "CreateResponseBodyText",
    "CreateResponseBodyTextVerbosity",
    "CreateResponseBodyToolChoice",
    "CreateResponseBodyTruncation",
    "DetailEnum",
    "DeveloperMessageItemParam",
    "DeveloperMessageItemParamContent",
    "DeveloperMessageItemParamRole",
    "DeveloperMessageItemParamType",
    "EmptyModelParam",
    "Error",
    "ErrorPayload",
    "ErrorStreamingEvent",
    "ErrorStreamingEventError",
    "ErrorStreamingEventType",
    "FunctionCall",
    "FunctionCallItemParam",
    "FunctionCallItemParamStatus",
    "FunctionCallItemParamType",
    "FunctionCallItemStatus",
    "FunctionCallOutput",
    "FunctionCallOutputItemParam",
    "FunctionCallOutputItemParamOutput",
    "FunctionCallOutputItemParamOutputOneItem",
    "FunctionCallOutputItemParamOutputOneItem_InputFile",
    "FunctionCallOutputItemParamOutputOneItem_InputImage",
    "FunctionCallOutputItemParamOutputOneItem_InputText",
    "FunctionCallOutputItemParamOutputOneItem_InputVideo",
    "FunctionCallOutputItemParamStatus",
    "FunctionCallOutputItemParamType",
    "FunctionCallOutputOutput",
    "FunctionCallOutputOutputOneItem",
    "FunctionCallOutputOutputOneItem_InputFile",
    "FunctionCallOutputOutputOneItem_InputImage",
    "FunctionCallOutputOutputOneItem_InputText",
    "FunctionCallOutputStatus",
    "FunctionCallOutputStatusEnum",
    "FunctionCallStatus",
    "FunctionTool",
    "FunctionToolChoice",
    "FunctionToolChoiceType",
    "FunctionToolParam",
    "FunctionToolParamType",
    "FunctionToolType",
    "ImageDetail",
    "IncludeEnum",
    "IncompleteDetails",
    "InputFileContent",
    "InputFileContentParam",
    "InputImageContent",
    "InputImageContentDetail",
    "InputImageContentParamAutoParam",
    "InputImageContentParamAutoParamDetail",
    "InputTextContent",
    "InputTextContentParam",
    "InputTextContentParamType",
    "InputTokensDetails",
    "InputVideoContent",
    "ItemField",
    "ItemField_FunctionCall",
    "ItemField_FunctionCallOutput",
    "ItemField_Message",
    "ItemField_Reasoning",
    "ItemParam",
    "ItemReferenceParam",
    "ItemReferenceParamType",
    "JsonObjectResponseFormat",
    "JsonSchemaResponseFormat",
    "JsonSchemaResponseFormatParam",
    "LogProb",
    "Message",
    "MessageContentItem",
    "MessageContentItem_InputFile",
    "MessageContentItem_InputImage",
    "MessageContentItem_InputText",
    "MessageContentItem_InputVideo",
    "MessageContentItem_OutputText",
    "MessageContentItem_ReasoningText",
    "MessageContentItem_Refusal",
    "MessageContentItem_SummaryText",
    "MessageContentItem_Text",
    "MessageRole",
    "MessageStatus",
    "MetadataParam",
    "OutputTextContent",
    "OutputTextContentParam",
    "OutputTokensDetails",
    "Reasoning",
    "ReasoningBody",
    "ReasoningBodyContentItem",
    "ReasoningBodyContentItem_InputFile",
    "ReasoningBodyContentItem_InputImage",
    "ReasoningBodyContentItem_InputText",
    "ReasoningBodyContentItem_OutputText",
    "ReasoningBodyContentItem_ReasoningText",
    "ReasoningBodyContentItem_Refusal",
    "ReasoningBodyContentItem_SummaryText",
    "ReasoningBodyContentItem_Text",
    "ReasoningBodySummaryItem",
    "ReasoningBodySummaryItem_InputFile",
    "ReasoningBodySummaryItem_InputImage",
    "ReasoningBodySummaryItem_InputText",
    "ReasoningBodySummaryItem_OutputText",
    "ReasoningBodySummaryItem_ReasoningText",
    "ReasoningBodySummaryItem_Refusal",
    "ReasoningBodySummaryItem_SummaryText",
    "ReasoningBodySummaryItem_Text",
    "ReasoningEffortEnum",
    "ReasoningItemParam",
    "ReasoningItemParamType",
    "ReasoningParam",
    "ReasoningParamSummary",
    "ReasoningSummary",
    "ReasoningSummaryContentParam",
    "ReasoningSummaryContentParamType",
    "ReasoningSummaryEnum",
    "ReasoningTextContent",
    "RefusalContent",
    "RefusalContentParam",
    "ResponseCompletedStreamingEvent",
    "ResponseCompletedStreamingEventResponse",
    "ResponseCompletedStreamingEventResponseError",
    "ResponseCompletedStreamingEventResponseIncompleteDetails",
    "ResponseCompletedStreamingEventResponseObject",
    "ResponseCompletedStreamingEventResponseReasoning",
    "ResponseCompletedStreamingEventResponseReasoningSummary",
    "ResponseCompletedStreamingEventResponseText",
    "ResponseCompletedStreamingEventResponseTextFormat",
    "ResponseCompletedStreamingEventResponseTextFormat_JsonObject",
    "ResponseCompletedStreamingEventResponseTextFormat_JsonSchema",
    "ResponseCompletedStreamingEventResponseTextFormat_Text",
    "ResponseCompletedStreamingEventResponseToolChoice",
    "ResponseCompletedStreamingEventResponseTruncation",
    "ResponseCompletedStreamingEventResponseUsage",
    "ResponseCompletedStreamingEventResponseUsageInputTokensDetails",
    "ResponseCompletedStreamingEventResponseUsageOutputTokensDetails",
    "ResponseCompletedStreamingEventType",
    "ResponseContentPartAddedStreamingEvent",
    "ResponseContentPartAddedStreamingEventPart",
    "ResponseContentPartAddedStreamingEventPart_InputFile",
    "ResponseContentPartAddedStreamingEventPart_InputImage",
    "ResponseContentPartAddedStreamingEventPart_InputText",
    "ResponseContentPartAddedStreamingEventPart_OutputText",
    "ResponseContentPartAddedStreamingEventPart_ReasoningText",
    "ResponseContentPartAddedStreamingEventPart_Refusal",
    "ResponseContentPartAddedStreamingEventPart_SummaryText",
    "ResponseContentPartAddedStreamingEventPart_Text",
    "ResponseContentPartAddedStreamingEventType",
    "ResponseContentPartDoneStreamingEvent",
    "ResponseContentPartDoneStreamingEventPart",
    "ResponseContentPartDoneStreamingEventPart_InputFile",
    "ResponseContentPartDoneStreamingEventPart_InputImage",
    "ResponseContentPartDoneStreamingEventPart_InputText",
    "ResponseContentPartDoneStreamingEventPart_OutputText",
    "ResponseContentPartDoneStreamingEventPart_ReasoningText",
    "ResponseContentPartDoneStreamingEventPart_Refusal",
    "ResponseContentPartDoneStreamingEventPart_SummaryText",
    "ResponseContentPartDoneStreamingEventPart_Text",
    "ResponseContentPartDoneStreamingEventType",
    "ResponseCreatedStreamingEvent",
    "ResponseCreatedStreamingEventResponse",
    "ResponseCreatedStreamingEventResponseError",
    "ResponseCreatedStreamingEventResponseIncompleteDetails",
    "ResponseCreatedStreamingEventResponseObject",
    "ResponseCreatedStreamingEventResponseReasoning",
    "ResponseCreatedStreamingEventResponseReasoningSummary",
    "ResponseCreatedStreamingEventResponseText",
    "ResponseCreatedStreamingEventResponseTextFormat",
    "ResponseCreatedStreamingEventResponseTextFormat_JsonObject",
    "ResponseCreatedStreamingEventResponseTextFormat_JsonSchema",
    "ResponseCreatedStreamingEventResponseTextFormat_Text",
    "ResponseCreatedStreamingEventResponseToolChoice",
    "ResponseCreatedStreamingEventResponseTruncation",
    "ResponseCreatedStreamingEventResponseUsage",
    "ResponseCreatedStreamingEventResponseUsageInputTokensDetails",
    "ResponseCreatedStreamingEventResponseUsageOutputTokensDetails",
    "ResponseCreatedStreamingEventType",
    "ResponseFailedStreamingEvent",
    "ResponseFailedStreamingEventResponse",
    "ResponseFailedStreamingEventResponseError",
    "ResponseFailedStreamingEventResponseIncompleteDetails",
    "ResponseFailedStreamingEventResponseObject",
    "ResponseFailedStreamingEventResponseReasoning",
    "ResponseFailedStreamingEventResponseReasoningSummary",
    "ResponseFailedStreamingEventResponseText",
    "ResponseFailedStreamingEventResponseTextFormat",
    "ResponseFailedStreamingEventResponseTextFormat_JsonObject",
    "ResponseFailedStreamingEventResponseTextFormat_JsonSchema",
    "ResponseFailedStreamingEventResponseTextFormat_Text",
    "ResponseFailedStreamingEventResponseToolChoice",
    "ResponseFailedStreamingEventResponseTruncation",
    "ResponseFailedStreamingEventResponseUsage",
    "ResponseFailedStreamingEventResponseUsageInputTokensDetails",
    "ResponseFailedStreamingEventResponseUsageOutputTokensDetails",
    "ResponseFailedStreamingEventType",
    "ResponseFunctionCallArgumentsDeltaStreamingEvent",
    "ResponseFunctionCallArgumentsDeltaStreamingEventType",
    "ResponseFunctionCallArgumentsDoneStreamingEvent",
    "ResponseFunctionCallArgumentsDoneStreamingEventType",
    "ResponseInProgressStreamingEvent",
    "ResponseInProgressStreamingEventResponse",
    "ResponseInProgressStreamingEventResponseError",
    "ResponseInProgressStreamingEventResponseIncompleteDetails",
    "ResponseInProgressStreamingEventResponseObject",
    "ResponseInProgressStreamingEventResponseReasoning",
    "ResponseInProgressStreamingEventResponseReasoningSummary",
    "ResponseInProgressStreamingEventResponseText",
    "ResponseInProgressStreamingEventResponseTextFormat",
    "ResponseInProgressStreamingEventResponseTextFormat_JsonObject",
    "ResponseInProgressStreamingEventResponseTextFormat_JsonSchema",
    "ResponseInProgressStreamingEventResponseTextFormat_Text",
    "ResponseInProgressStreamingEventResponseToolChoice",
    "ResponseInProgressStreamingEventResponseTruncation",
    "ResponseInProgressStreamingEventResponseUsage",
    "ResponseInProgressStreamingEventResponseUsageInputTokensDetails",
    "ResponseInProgressStreamingEventResponseUsageOutputTokensDetails",
    "ResponseInProgressStreamingEventType",
    "ResponseIncompleteStreamingEvent",
    "ResponseIncompleteStreamingEventResponse",
    "ResponseIncompleteStreamingEventResponseError",
    "ResponseIncompleteStreamingEventResponseIncompleteDetails",
    "ResponseIncompleteStreamingEventResponseObject",
    "ResponseIncompleteStreamingEventResponseReasoning",
    "ResponseIncompleteStreamingEventResponseReasoningSummary",
    "ResponseIncompleteStreamingEventResponseText",
    "ResponseIncompleteStreamingEventResponseTextFormat",
    "ResponseIncompleteStreamingEventResponseTextFormat_JsonObject",
    "ResponseIncompleteStreamingEventResponseTextFormat_JsonSchema",
    "ResponseIncompleteStreamingEventResponseTextFormat_Text",
    "ResponseIncompleteStreamingEventResponseToolChoice",
    "ResponseIncompleteStreamingEventResponseTruncation",
    "ResponseIncompleteStreamingEventResponseUsage",
    "ResponseIncompleteStreamingEventResponseUsageInputTokensDetails",
    "ResponseIncompleteStreamingEventResponseUsageOutputTokensDetails",
    "ResponseIncompleteStreamingEventType",
    "ResponseOutputItemAddedStreamingEvent",
    "ResponseOutputItemAddedStreamingEventItem",
    "ResponseOutputItemAddedStreamingEventItem_FunctionCall",
    "ResponseOutputItemAddedStreamingEventItem_FunctionCallOutput",
    "ResponseOutputItemAddedStreamingEventItem_Message",
    "ResponseOutputItemAddedStreamingEventItem_Reasoning",
    "ResponseOutputItemAddedStreamingEventType",
    "ResponseOutputItemDoneStreamingEvent",
    "ResponseOutputItemDoneStreamingEventItem",
    "ResponseOutputItemDoneStreamingEventItem_FunctionCall",
    "ResponseOutputItemDoneStreamingEventItem_FunctionCallOutput",
    "ResponseOutputItemDoneStreamingEventItem_Message",
    "ResponseOutputItemDoneStreamingEventItem_Reasoning",
    "ResponseOutputItemDoneStreamingEventType",
    "ResponseOutputTextAnnotationAddedStreamingEvent",
    "ResponseOutputTextAnnotationAddedStreamingEventType",
    "ResponseOutputTextDeltaStreamingEvent",
    "ResponseOutputTextDeltaStreamingEventType",
    "ResponseOutputTextDoneStreamingEvent",
    "ResponseOutputTextDoneStreamingEventType",
    "ResponseQueuedStreamingEvent",
    "ResponseQueuedStreamingEventResponse",
    "ResponseQueuedStreamingEventResponseError",
    "ResponseQueuedStreamingEventResponseIncompleteDetails",
    "ResponseQueuedStreamingEventResponseObject",
    "ResponseQueuedStreamingEventResponseReasoning",
    "ResponseQueuedStreamingEventResponseReasoningSummary",
    "ResponseQueuedStreamingEventResponseText",
    "ResponseQueuedStreamingEventResponseTextFormat",
    "ResponseQueuedStreamingEventResponseTextFormat_JsonObject",
    "ResponseQueuedStreamingEventResponseTextFormat_JsonSchema",
    "ResponseQueuedStreamingEventResponseTextFormat_Text",
    "ResponseQueuedStreamingEventResponseToolChoice",
    "ResponseQueuedStreamingEventResponseTruncation",
    "ResponseQueuedStreamingEventResponseUsage",
    "ResponseQueuedStreamingEventResponseUsageInputTokensDetails",
    "ResponseQueuedStreamingEventResponseUsageOutputTokensDetails",
    "ResponseQueuedStreamingEventType",
    "ResponseReasoningDeltaStreamingEvent",
    "ResponseReasoningDeltaStreamingEventType",
    "ResponseReasoningDoneStreamingEvent",
    "ResponseReasoningDoneStreamingEventType",
    "ResponseReasoningSummaryDeltaStreamingEvent",
    "ResponseReasoningSummaryDeltaStreamingEventType",
    "ResponseReasoningSummaryDoneStreamingEvent",
    "ResponseReasoningSummaryDoneStreamingEventType",
    "ResponseReasoningSummaryPartAddedStreamingEvent",
    "ResponseReasoningSummaryPartAddedStreamingEventPart",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_InputFile",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_InputImage",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_InputText",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_OutputText",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_ReasoningText",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_Refusal",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_SummaryText",
    "ResponseReasoningSummaryPartAddedStreamingEventPart_Text",
    "ResponseReasoningSummaryPartAddedStreamingEventType",
    "ResponseReasoningSummaryPartDoneStreamingEvent",
    "ResponseReasoningSummaryPartDoneStreamingEventPart",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_InputFile",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_InputImage",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_InputText",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_OutputText",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_ReasoningText",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_Refusal",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_SummaryText",
    "ResponseReasoningSummaryPartDoneStreamingEventPart_Text",
    "ResponseReasoningSummaryPartDoneStreamingEventType",
    "ResponseRefusalDeltaStreamingEvent",
    "ResponseRefusalDeltaStreamingEventType",
    "ResponseRefusalDoneStreamingEvent",
    "ResponseRefusalDoneStreamingEventType",
    "ResponseResource",
    "ResponseResourceError",
    "ResponseResourceIncompleteDetails",
    "ResponseResourceObject",
    "ResponseResourceReasoning",
    "ResponseResourceReasoningSummary",
    "ResponseResourceText",
    "ResponseResourceTextFormat",
    "ResponseResourceTextFormat_JsonObject",
    "ResponseResourceTextFormat_JsonSchema",
    "ResponseResourceTextFormat_Text",
    "ResponseResourceToolChoice",
    "ResponseResourceTruncation",
    "ResponseResourceUsage",
    "ResponseResourceUsageInputTokensDetails",
    "ResponseResourceUsageOutputTokensDetails",
    "ResponsesToolParam",
    "ServiceTierEnum",
    "SpecificFunctionParam",
    "SpecificFunctionParamType",
    "SpecificToolChoiceParam",
    "StreamOptionsParam",
    "SummaryTextContent",
    "SystemMessageItemParam",
    "SystemMessageItemParamContent",
    "SystemMessageItemParamRole",
    "SystemMessageItemParamType",
    "TextContent",
    "TextField",
    "TextFieldFormat",
    "TextFieldFormat_JsonObject",
    "TextFieldFormat_JsonSchema",
    "TextFieldFormat_Text",
    "TextFormatParam",
    "TextFormatParam_JsonSchema",
    "TextFormatParam_Text",
    "TextParam",
    "TextParamVerbosity",
    "TextResponseFormat",
    "Tool",
    "ToolChoiceParam",
    "ToolChoiceValueEnum",
    "TopLogProb",
    "TruncationEnum",
    "UrlCitationBody",
    "UrlCitationBodyType",
    "UrlCitationParam",
    "UrlCitationParamType",
    "Usage",
    "UsageInputTokensDetails",
    "UsageOutputTokensDetails",
    "UserMessageItemParam",
    "UserMessageItemParamContent",
    "UserMessageItemParamContentZeroItem",
    "UserMessageItemParamContentZeroItem_InputFile",
    "UserMessageItemParamContentZeroItem_InputImage",
    "UserMessageItemParamContentZeroItem_InputText",
    "UserMessageItemParamRole",
    "UserMessageItemParamType",
    "VerbosityEnum",
]
