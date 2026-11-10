



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .assistant_file_object import AssistantFileObject
    from .assistant_file_object_object import AssistantFileObjectObject
    from .assistant_object import AssistantObject
    from .assistant_object_object import AssistantObjectObject
    from .assistant_object_tools_item import (
        AssistantObjectToolsItem,
        AssistantObjectToolsItem_CodeInterpreter,
        AssistantObjectToolsItem_Function,
        AssistantObjectToolsItem_Retrieval,
    )
    from .assistant_stream_event import AssistantStreamEvent
    from .assistant_tools_code import AssistantToolsCode
    from .assistant_tools_function import AssistantToolsFunction
    from .assistant_tools_retrieval import AssistantToolsRetrieval
    from .assistants_api_named_tool_choice import AssistantsApiNamedToolChoice
    from .assistants_api_named_tool_choice_function import AssistantsApiNamedToolChoiceFunction
    from .assistants_api_named_tool_choice_type import AssistantsApiNamedToolChoiceType
    from .assistants_api_response_format import AssistantsApiResponseFormat
    from .assistants_api_response_format_option import AssistantsApiResponseFormatOption
    from .assistants_api_response_format_option_zero import AssistantsApiResponseFormatOptionZero
    from .assistants_api_response_format_type import AssistantsApiResponseFormatType
    from .assistants_api_tool_choice_option import AssistantsApiToolChoiceOption
    from .assistants_api_tool_choice_option_zero import AssistantsApiToolChoiceOptionZero
    from .chat_completion_function_call_option import ChatCompletionFunctionCallOption
    from .chat_completion_functions import ChatCompletionFunctions
    from .chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from .chat_completion_message_tool_call_chunk import ChatCompletionMessageToolCallChunk
    from .chat_completion_message_tool_call_chunk_function import ChatCompletionMessageToolCallChunkFunction
    from .chat_completion_message_tool_call_chunk_type import ChatCompletionMessageToolCallChunkType
    from .chat_completion_message_tool_call_function import ChatCompletionMessageToolCallFunction
    from .chat_completion_message_tool_call_type import ChatCompletionMessageToolCallType
    from .chat_completion_message_tool_calls import ChatCompletionMessageToolCalls
    from .chat_completion_named_tool_choice import ChatCompletionNamedToolChoice
    from .chat_completion_named_tool_choice_function import ChatCompletionNamedToolChoiceFunction
    from .chat_completion_named_tool_choice_type import ChatCompletionNamedToolChoiceType
    from .chat_completion_request_assistant_message import ChatCompletionRequestAssistantMessage
    from .chat_completion_request_assistant_message_function_call import (
        ChatCompletionRequestAssistantMessageFunctionCall,
    )
    from .chat_completion_request_function_message import ChatCompletionRequestFunctionMessage
    from .chat_completion_request_message import (
        ChatCompletionRequestMessage,
        ChatCompletionRequestMessage_Assistant,
        ChatCompletionRequestMessage_Function,
        ChatCompletionRequestMessage_System,
        ChatCompletionRequestMessage_Tool,
        ChatCompletionRequestMessage_User,
    )
    from .chat_completion_request_message_content_part import (
        ChatCompletionRequestMessageContentPart,
        ChatCompletionRequestMessageContentPart_ImageUrl,
        ChatCompletionRequestMessageContentPart_Text,
    )
    from .chat_completion_request_message_content_part_image import ChatCompletionRequestMessageContentPartImage
    from .chat_completion_request_message_content_part_image_image_url import (
        ChatCompletionRequestMessageContentPartImageImageUrl,
    )
    from .chat_completion_request_message_content_part_image_image_url_detail import (
        ChatCompletionRequestMessageContentPartImageImageUrlDetail,
    )
    from .chat_completion_request_message_content_part_text import ChatCompletionRequestMessageContentPartText
    from .chat_completion_request_system_message import ChatCompletionRequestSystemMessage
    from .chat_completion_request_tool_message import ChatCompletionRequestToolMessage
    from .chat_completion_request_user_message import ChatCompletionRequestUserMessage
    from .chat_completion_request_user_message_content import ChatCompletionRequestUserMessageContent
    from .chat_completion_response_message import ChatCompletionResponseMessage
    from .chat_completion_response_message_function_call import ChatCompletionResponseMessageFunctionCall
    from .chat_completion_response_message_role import ChatCompletionResponseMessageRole
    from .chat_completion_role import ChatCompletionRole
    from .chat_completion_stream_response_delta import ChatCompletionStreamResponseDelta
    from .chat_completion_stream_response_delta_function_call import ChatCompletionStreamResponseDeltaFunctionCall
    from .chat_completion_stream_response_delta_role import ChatCompletionStreamResponseDeltaRole
    from .chat_completion_token_logprob import ChatCompletionTokenLogprob
    from .chat_completion_token_logprob_top_logprobs_item import ChatCompletionTokenLogprobTopLogprobsItem
    from .chat_completion_tool import ChatCompletionTool
    from .chat_completion_tool_choice_option import ChatCompletionToolChoiceOption
    from .chat_completion_tool_choice_option_zero import ChatCompletionToolChoiceOptionZero
    from .chat_completion_tool_type import ChatCompletionToolType
    from .completion_usage import CompletionUsage
    from .create_chat_completion_function_response import CreateChatCompletionFunctionResponse
    from .create_chat_completion_function_response_choices_item import CreateChatCompletionFunctionResponseChoicesItem
    from .create_chat_completion_function_response_choices_item_finish_reason import (
        CreateChatCompletionFunctionResponseChoicesItemFinishReason,
    )
    from .create_chat_completion_function_response_object import CreateChatCompletionFunctionResponseObject
    from .create_chat_completion_image_response import CreateChatCompletionImageResponse
    from .create_chat_completion_response import CreateChatCompletionResponse
    from .create_chat_completion_response_choices_item import CreateChatCompletionResponseChoicesItem
    from .create_chat_completion_response_choices_item_finish_reason import (
        CreateChatCompletionResponseChoicesItemFinishReason,
    )
    from .create_chat_completion_response_choices_item_logprobs import CreateChatCompletionResponseChoicesItemLogprobs
    from .create_chat_completion_response_object import CreateChatCompletionResponseObject
    from .create_chat_completion_stream_response import CreateChatCompletionStreamResponse
    from .create_chat_completion_stream_response_choices_item import CreateChatCompletionStreamResponseChoicesItem
    from .create_chat_completion_stream_response_choices_item_finish_reason import (
        CreateChatCompletionStreamResponseChoicesItemFinishReason,
    )
    from .create_chat_completion_stream_response_choices_item_logprobs import (
        CreateChatCompletionStreamResponseChoicesItemLogprobs,
    )
    from .create_chat_completion_stream_response_object import CreateChatCompletionStreamResponseObject
    from .create_completion_response import CreateCompletionResponse
    from .create_completion_response_choices_item import CreateCompletionResponseChoicesItem
    from .create_completion_response_choices_item_finish_reason import CreateCompletionResponseChoicesItemFinishReason
    from .create_completion_response_choices_item_logprobs import CreateCompletionResponseChoicesItemLogprobs
    from .create_completion_response_object import CreateCompletionResponseObject
    from .create_embedding_response import CreateEmbeddingResponse
    from .create_embedding_response_object import CreateEmbeddingResponseObject
    from .create_embedding_response_usage import CreateEmbeddingResponseUsage
    from .create_message_request import CreateMessageRequest
    from .create_message_request_role import CreateMessageRequestRole
    from .create_moderation_response import CreateModerationResponse
    from .create_moderation_response_results_item import CreateModerationResponseResultsItem
    from .create_moderation_response_results_item_categories import CreateModerationResponseResultsItemCategories
    from .create_moderation_response_results_item_category_scores import (
        CreateModerationResponseResultsItemCategoryScores,
    )
    from .create_thread_request import CreateThreadRequest
    from .create_transcription_response_json import CreateTranscriptionResponseJson
    from .create_transcription_response_verbose_json import CreateTranscriptionResponseVerboseJson
    from .create_translation_response_json import CreateTranslationResponseJson
    from .create_translation_response_verbose_json import CreateTranslationResponseVerboseJson
    from .delete_assistant_file_response import DeleteAssistantFileResponse
    from .delete_assistant_file_response_object import DeleteAssistantFileResponseObject
    from .delete_assistant_response import DeleteAssistantResponse
    from .delete_assistant_response_object import DeleteAssistantResponseObject
    from .delete_file_response import DeleteFileResponse
    from .delete_file_response_object import DeleteFileResponseObject
    from .delete_message_response import DeleteMessageResponse
    from .delete_message_response_object import DeleteMessageResponseObject
    from .delete_model_response import DeleteModelResponse
    from .delete_thread_response import DeleteThreadResponse
    from .delete_thread_response_object import DeleteThreadResponseObject
    from .done_event import DoneEvent
    from .done_event_data import DoneEventData
    from .done_event_event import DoneEventEvent
    from .embedding import Embedding
    from .embedding_object import EmbeddingObject
    from .error import Error
    from .error_event import ErrorEvent
    from .error_event_event import ErrorEventEvent
    from .error_response import ErrorResponse
    from .fine_tuning_integration import FineTuningIntegration
    from .fine_tuning_integration_type import FineTuningIntegrationType
    from .fine_tuning_integration_wandb import FineTuningIntegrationWandb
    from .fine_tuning_job import FineTuningJob
    from .fine_tuning_job_checkpoint import FineTuningJobCheckpoint
    from .fine_tuning_job_checkpoint_metrics import FineTuningJobCheckpointMetrics
    from .fine_tuning_job_checkpoint_object import FineTuningJobCheckpointObject
    from .fine_tuning_job_error import FineTuningJobError
    from .fine_tuning_job_event import FineTuningJobEvent
    from .fine_tuning_job_event_level import FineTuningJobEventLevel
    from .fine_tuning_job_event_object import FineTuningJobEventObject
    from .fine_tuning_job_hyperparameters import FineTuningJobHyperparameters
    from .fine_tuning_job_hyperparameters_n_epochs import FineTuningJobHyperparametersNEpochs
    from .fine_tuning_job_hyperparameters_n_epochs_zero import FineTuningJobHyperparametersNEpochsZero
    from .fine_tuning_job_object import FineTuningJobObject
    from .fine_tuning_job_status import FineTuningJobStatus
    from .function_object import FunctionObject
    from .function_parameters import FunctionParameters
    from .image import Image
    from .images_response import ImagesResponse
    from .list_assistant_files_response import ListAssistantFilesResponse
    from .list_assistants_response import ListAssistantsResponse
    from .list_files_response import ListFilesResponse
    from .list_files_response_object import ListFilesResponseObject
    from .list_fine_tuning_job_checkpoints_response import ListFineTuningJobCheckpointsResponse
    from .list_fine_tuning_job_checkpoints_response_object import ListFineTuningJobCheckpointsResponseObject
    from .list_fine_tuning_job_events_response import ListFineTuningJobEventsResponse
    from .list_fine_tuning_job_events_response_object import ListFineTuningJobEventsResponseObject
    from .list_message_files_response import ListMessageFilesResponse
    from .list_messages_response import ListMessagesResponse
    from .list_models_response import ListModelsResponse
    from .list_models_response_object import ListModelsResponseObject
    from .list_paginated_fine_tuning_jobs_response import ListPaginatedFineTuningJobsResponse
    from .list_paginated_fine_tuning_jobs_response_object import ListPaginatedFineTuningJobsResponseObject
    from .list_run_steps_response import ListRunStepsResponse
    from .list_runs_response import ListRunsResponse
    from .list_threads_response import ListThreadsResponse
    from .message_content_image_file_object import MessageContentImageFileObject
    from .message_content_image_file_object_image_file import MessageContentImageFileObjectImageFile
    from .message_content_text_annotations_file_citation_object import MessageContentTextAnnotationsFileCitationObject
    from .message_content_text_annotations_file_citation_object_file_citation import (
        MessageContentTextAnnotationsFileCitationObjectFileCitation,
    )
    from .message_content_text_annotations_file_path_object import MessageContentTextAnnotationsFilePathObject
    from .message_content_text_annotations_file_path_object_file_path import (
        MessageContentTextAnnotationsFilePathObjectFilePath,
    )
    from .message_content_text_object import MessageContentTextObject
    from .message_content_text_object_text import MessageContentTextObjectText
    from .message_content_text_object_text_annotations_item import (
        MessageContentTextObjectTextAnnotationsItem,
        MessageContentTextObjectTextAnnotationsItem_FileCitation,
        MessageContentTextObjectTextAnnotationsItem_FilePath,
    )
    from .message_delta_content_image_file_object import MessageDeltaContentImageFileObject
    from .message_delta_content_image_file_object_image_file import MessageDeltaContentImageFileObjectImageFile
    from .message_delta_content_text_annotations_file_citation_object import (
        MessageDeltaContentTextAnnotationsFileCitationObject,
    )
    from .message_delta_content_text_annotations_file_citation_object_file_citation import (
        MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation,
    )
    from .message_delta_content_text_annotations_file_path_object import (
        MessageDeltaContentTextAnnotationsFilePathObject,
    )
    from .message_delta_content_text_annotations_file_path_object_file_path import (
        MessageDeltaContentTextAnnotationsFilePathObjectFilePath,
    )
    from .message_delta_content_text_object import MessageDeltaContentTextObject
    from .message_delta_content_text_object_text import MessageDeltaContentTextObjectText
    from .message_delta_content_text_object_text_annotations_item import (
        MessageDeltaContentTextObjectTextAnnotationsItem,
        MessageDeltaContentTextObjectTextAnnotationsItem_FileCitation,
        MessageDeltaContentTextObjectTextAnnotationsItem_FilePath,
    )
    from .message_delta_object import MessageDeltaObject
    from .message_delta_object_delta import MessageDeltaObjectDelta
    from .message_delta_object_delta_content_item import (
        MessageDeltaObjectDeltaContentItem,
        MessageDeltaObjectDeltaContentItem_ImageFile,
        MessageDeltaObjectDeltaContentItem_Text,
    )
    from .message_delta_object_delta_role import MessageDeltaObjectDeltaRole
    from .message_delta_object_object import MessageDeltaObjectObject
    from .message_file_object import MessageFileObject
    from .message_file_object_object import MessageFileObjectObject
    from .message_object import MessageObject
    from .message_object_content_item import (
        MessageObjectContentItem,
        MessageObjectContentItem_ImageFile,
        MessageObjectContentItem_Text,
    )
    from .message_object_incomplete_details import MessageObjectIncompleteDetails
    from .message_object_incomplete_details_reason import MessageObjectIncompleteDetailsReason
    from .message_object_object import MessageObjectObject
    from .message_object_role import MessageObjectRole
    from .message_object_status import MessageObjectStatus
    from .message_stream_event import (
        MessageStreamEvent,
        MessageStreamEvent_ThreadMessageCompleted,
        MessageStreamEvent_ThreadMessageCreated,
        MessageStreamEvent_ThreadMessageDelta,
        MessageStreamEvent_ThreadMessageInProgress,
        MessageStreamEvent_ThreadMessageIncomplete,
    )
    from .message_stream_event_thread_message_completed import MessageStreamEventThreadMessageCompleted
    from .message_stream_event_thread_message_created import MessageStreamEventThreadMessageCreated
    from .message_stream_event_thread_message_delta import MessageStreamEventThreadMessageDelta
    from .message_stream_event_thread_message_in_progress import MessageStreamEventThreadMessageInProgress
    from .message_stream_event_thread_message_incomplete import MessageStreamEventThreadMessageIncomplete
    from .model import Model
    from .model_object import ModelObject
    from .open_ai_file import OpenAiFile
    from .open_ai_file_object import OpenAiFileObject
    from .open_ai_file_purpose import OpenAiFilePurpose
    from .open_ai_file_status import OpenAiFileStatus
    from .run_completion_usage import RunCompletionUsage
    from .run_object import RunObject
    from .run_object_incomplete_details import RunObjectIncompleteDetails
    from .run_object_incomplete_details_reason import RunObjectIncompleteDetailsReason
    from .run_object_last_error import RunObjectLastError
    from .run_object_last_error_code import RunObjectLastErrorCode
    from .run_object_object import RunObjectObject
    from .run_object_required_action import RunObjectRequiredAction
    from .run_object_required_action_submit_tool_outputs import RunObjectRequiredActionSubmitToolOutputs
    from .run_object_required_action_type import RunObjectRequiredActionType
    from .run_object_status import RunObjectStatus
    from .run_object_tools_item import (
        RunObjectToolsItem,
        RunObjectToolsItem_CodeInterpreter,
        RunObjectToolsItem_Function,
        RunObjectToolsItem_Retrieval,
    )
    from .run_step_completion_usage import RunStepCompletionUsage
    from .run_step_delta_object import RunStepDeltaObject
    from .run_step_delta_object_delta import RunStepDeltaObjectDelta
    from .run_step_delta_object_delta_step_details import (
        RunStepDeltaObjectDeltaStepDetails,
        RunStepDeltaObjectDeltaStepDetails_MessageCreation,
        RunStepDeltaObjectDeltaStepDetails_ToolCalls,
    )
    from .run_step_delta_object_object import RunStepDeltaObjectObject
    from .run_step_delta_step_details_message_creation_object import RunStepDeltaStepDetailsMessageCreationObject
    from .run_step_delta_step_details_message_creation_object_message_creation import (
        RunStepDeltaStepDetailsMessageCreationObjectMessageCreation,
    )
    from .run_step_delta_step_details_tool_calls_code_object import RunStepDeltaStepDetailsToolCallsCodeObject
    from .run_step_delta_step_details_tool_calls_code_object_code_interpreter import (
        RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter,
    )
    from .run_step_delta_step_details_tool_calls_code_object_code_interpreter_outputs_item import (
        RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem,
        RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image,
        RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs,
    )
    from .run_step_delta_step_details_tool_calls_code_output_image_object import (
        RunStepDeltaStepDetailsToolCallsCodeOutputImageObject,
    )
    from .run_step_delta_step_details_tool_calls_code_output_image_object_image import (
        RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage,
    )
    from .run_step_delta_step_details_tool_calls_code_output_logs_object import (
        RunStepDeltaStepDetailsToolCallsCodeOutputLogsObject,
    )
    from .run_step_delta_step_details_tool_calls_function_object import RunStepDeltaStepDetailsToolCallsFunctionObject
    from .run_step_delta_step_details_tool_calls_function_object_function import (
        RunStepDeltaStepDetailsToolCallsFunctionObjectFunction,
    )
    from .run_step_delta_step_details_tool_calls_object import RunStepDeltaStepDetailsToolCallsObject
    from .run_step_delta_step_details_tool_calls_object_tool_calls_item import (
        RunStepDeltaStepDetailsToolCallsObjectToolCallsItem,
        RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter,
        RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Function,
        RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Retrieval,
    )
    from .run_step_delta_step_details_tool_calls_retrieval_object import RunStepDeltaStepDetailsToolCallsRetrievalObject
    from .run_step_details_message_creation_object import RunStepDetailsMessageCreationObject
    from .run_step_details_message_creation_object_message_creation import (
        RunStepDetailsMessageCreationObjectMessageCreation,
    )
    from .run_step_details_tool_calls_code_object import RunStepDetailsToolCallsCodeObject
    from .run_step_details_tool_calls_code_object_code_interpreter import (
        RunStepDetailsToolCallsCodeObjectCodeInterpreter,
    )
    from .run_step_details_tool_calls_code_object_code_interpreter_outputs_item import (
        RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem,
        RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image,
        RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs,
    )
    from .run_step_details_tool_calls_code_output_image_object import RunStepDetailsToolCallsCodeOutputImageObject
    from .run_step_details_tool_calls_code_output_image_object_image import (
        RunStepDetailsToolCallsCodeOutputImageObjectImage,
    )
    from .run_step_details_tool_calls_code_output_logs_object import RunStepDetailsToolCallsCodeOutputLogsObject
    from .run_step_details_tool_calls_function_object import RunStepDetailsToolCallsFunctionObject
    from .run_step_details_tool_calls_function_object_function import RunStepDetailsToolCallsFunctionObjectFunction
    from .run_step_details_tool_calls_object import RunStepDetailsToolCallsObject
    from .run_step_details_tool_calls_object_tool_calls_item import (
        RunStepDetailsToolCallsObjectToolCallsItem,
        RunStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter,
        RunStepDetailsToolCallsObjectToolCallsItem_Function,
        RunStepDetailsToolCallsObjectToolCallsItem_Retrieval,
    )
    from .run_step_details_tool_calls_retrieval_object import RunStepDetailsToolCallsRetrievalObject
    from .run_step_object import RunStepObject
    from .run_step_object_last_error import RunStepObjectLastError
    from .run_step_object_last_error_code import RunStepObjectLastErrorCode
    from .run_step_object_object import RunStepObjectObject
    from .run_step_object_status import RunStepObjectStatus
    from .run_step_object_step_details import (
        RunStepObjectStepDetails,
        RunStepObjectStepDetails_MessageCreation,
        RunStepObjectStepDetails_ToolCalls,
    )
    from .run_step_object_type import RunStepObjectType
    from .run_step_stream_event import (
        RunStepStreamEvent,
        RunStepStreamEvent_ThreadRunStepCancelled,
        RunStepStreamEvent_ThreadRunStepCompleted,
        RunStepStreamEvent_ThreadRunStepCreated,
        RunStepStreamEvent_ThreadRunStepDelta,
        RunStepStreamEvent_ThreadRunStepExpired,
        RunStepStreamEvent_ThreadRunStepFailed,
        RunStepStreamEvent_ThreadRunStepInProgress,
    )
    from .run_step_stream_event_thread_run_step_cancelled import RunStepStreamEventThreadRunStepCancelled
    from .run_step_stream_event_thread_run_step_completed import RunStepStreamEventThreadRunStepCompleted
    from .run_step_stream_event_thread_run_step_created import RunStepStreamEventThreadRunStepCreated
    from .run_step_stream_event_thread_run_step_delta import RunStepStreamEventThreadRunStepDelta
    from .run_step_stream_event_thread_run_step_expired import RunStepStreamEventThreadRunStepExpired
    from .run_step_stream_event_thread_run_step_failed import RunStepStreamEventThreadRunStepFailed
    from .run_step_stream_event_thread_run_step_in_progress import RunStepStreamEventThreadRunStepInProgress
    from .run_stream_event import (
        RunStreamEvent,
        RunStreamEvent_ThreadRunCancelled,
        RunStreamEvent_ThreadRunCancelling,
        RunStreamEvent_ThreadRunCompleted,
        RunStreamEvent_ThreadRunCreated,
        RunStreamEvent_ThreadRunExpired,
        RunStreamEvent_ThreadRunFailed,
        RunStreamEvent_ThreadRunInProgress,
        RunStreamEvent_ThreadRunQueued,
        RunStreamEvent_ThreadRunRequiresAction,
    )
    from .run_stream_event_thread_run_cancelled import RunStreamEventThreadRunCancelled
    from .run_stream_event_thread_run_cancelling import RunStreamEventThreadRunCancelling
    from .run_stream_event_thread_run_completed import RunStreamEventThreadRunCompleted
    from .run_stream_event_thread_run_created import RunStreamEventThreadRunCreated
    from .run_stream_event_thread_run_expired import RunStreamEventThreadRunExpired
    from .run_stream_event_thread_run_failed import RunStreamEventThreadRunFailed
    from .run_stream_event_thread_run_in_progress import RunStreamEventThreadRunInProgress
    from .run_stream_event_thread_run_queued import RunStreamEventThreadRunQueued
    from .run_stream_event_thread_run_requires_action import RunStreamEventThreadRunRequiresAction
    from .run_tool_call_object import RunToolCallObject
    from .run_tool_call_object_function import RunToolCallObjectFunction
    from .run_tool_call_object_type import RunToolCallObjectType
    from .thread_object import ThreadObject
    from .thread_object_object import ThreadObjectObject
    from .thread_stream_event import ThreadStreamEvent
    from .thread_stream_event_event import ThreadStreamEventEvent
    from .transcription_segment import TranscriptionSegment
    from .transcription_word import TranscriptionWord
    from .truncation_object import TruncationObject
    from .truncation_object_type import TruncationObjectType
_dynamic_imports: typing.Dict[str, str] = {
    "AssistantFileObject": ".assistant_file_object",
    "AssistantFileObjectObject": ".assistant_file_object_object",
    "AssistantObject": ".assistant_object",
    "AssistantObjectObject": ".assistant_object_object",
    "AssistantObjectToolsItem": ".assistant_object_tools_item",
    "AssistantObjectToolsItem_CodeInterpreter": ".assistant_object_tools_item",
    "AssistantObjectToolsItem_Function": ".assistant_object_tools_item",
    "AssistantObjectToolsItem_Retrieval": ".assistant_object_tools_item",
    "AssistantStreamEvent": ".assistant_stream_event",
    "AssistantToolsCode": ".assistant_tools_code",
    "AssistantToolsFunction": ".assistant_tools_function",
    "AssistantToolsRetrieval": ".assistant_tools_retrieval",
    "AssistantsApiNamedToolChoice": ".assistants_api_named_tool_choice",
    "AssistantsApiNamedToolChoiceFunction": ".assistants_api_named_tool_choice_function",
    "AssistantsApiNamedToolChoiceType": ".assistants_api_named_tool_choice_type",
    "AssistantsApiResponseFormat": ".assistants_api_response_format",
    "AssistantsApiResponseFormatOption": ".assistants_api_response_format_option",
    "AssistantsApiResponseFormatOptionZero": ".assistants_api_response_format_option_zero",
    "AssistantsApiResponseFormatType": ".assistants_api_response_format_type",
    "AssistantsApiToolChoiceOption": ".assistants_api_tool_choice_option",
    "AssistantsApiToolChoiceOptionZero": ".assistants_api_tool_choice_option_zero",
    "ChatCompletionFunctionCallOption": ".chat_completion_function_call_option",
    "ChatCompletionFunctions": ".chat_completion_functions",
    "ChatCompletionMessageToolCall": ".chat_completion_message_tool_call",
    "ChatCompletionMessageToolCallChunk": ".chat_completion_message_tool_call_chunk",
    "ChatCompletionMessageToolCallChunkFunction": ".chat_completion_message_tool_call_chunk_function",
    "ChatCompletionMessageToolCallChunkType": ".chat_completion_message_tool_call_chunk_type",
    "ChatCompletionMessageToolCallFunction": ".chat_completion_message_tool_call_function",
    "ChatCompletionMessageToolCallType": ".chat_completion_message_tool_call_type",
    "ChatCompletionMessageToolCalls": ".chat_completion_message_tool_calls",
    "ChatCompletionNamedToolChoice": ".chat_completion_named_tool_choice",
    "ChatCompletionNamedToolChoiceFunction": ".chat_completion_named_tool_choice_function",
    "ChatCompletionNamedToolChoiceType": ".chat_completion_named_tool_choice_type",
    "ChatCompletionRequestAssistantMessage": ".chat_completion_request_assistant_message",
    "ChatCompletionRequestAssistantMessageFunctionCall": ".chat_completion_request_assistant_message_function_call",
    "ChatCompletionRequestFunctionMessage": ".chat_completion_request_function_message",
    "ChatCompletionRequestMessage": ".chat_completion_request_message",
    "ChatCompletionRequestMessageContentPart": ".chat_completion_request_message_content_part",
    "ChatCompletionRequestMessageContentPartImage": ".chat_completion_request_message_content_part_image",
    "ChatCompletionRequestMessageContentPartImageImageUrl": ".chat_completion_request_message_content_part_image_image_url",
    "ChatCompletionRequestMessageContentPartImageImageUrlDetail": ".chat_completion_request_message_content_part_image_image_url_detail",
    "ChatCompletionRequestMessageContentPartText": ".chat_completion_request_message_content_part_text",
    "ChatCompletionRequestMessageContentPart_ImageUrl": ".chat_completion_request_message_content_part",
    "ChatCompletionRequestMessageContentPart_Text": ".chat_completion_request_message_content_part",
    "ChatCompletionRequestMessage_Assistant": ".chat_completion_request_message",
    "ChatCompletionRequestMessage_Function": ".chat_completion_request_message",
    "ChatCompletionRequestMessage_System": ".chat_completion_request_message",
    "ChatCompletionRequestMessage_Tool": ".chat_completion_request_message",
    "ChatCompletionRequestMessage_User": ".chat_completion_request_message",
    "ChatCompletionRequestSystemMessage": ".chat_completion_request_system_message",
    "ChatCompletionRequestToolMessage": ".chat_completion_request_tool_message",
    "ChatCompletionRequestUserMessage": ".chat_completion_request_user_message",
    "ChatCompletionRequestUserMessageContent": ".chat_completion_request_user_message_content",
    "ChatCompletionResponseMessage": ".chat_completion_response_message",
    "ChatCompletionResponseMessageFunctionCall": ".chat_completion_response_message_function_call",
    "ChatCompletionResponseMessageRole": ".chat_completion_response_message_role",
    "ChatCompletionRole": ".chat_completion_role",
    "ChatCompletionStreamResponseDelta": ".chat_completion_stream_response_delta",
    "ChatCompletionStreamResponseDeltaFunctionCall": ".chat_completion_stream_response_delta_function_call",
    "ChatCompletionStreamResponseDeltaRole": ".chat_completion_stream_response_delta_role",
    "ChatCompletionTokenLogprob": ".chat_completion_token_logprob",
    "ChatCompletionTokenLogprobTopLogprobsItem": ".chat_completion_token_logprob_top_logprobs_item",
    "ChatCompletionTool": ".chat_completion_tool",
    "ChatCompletionToolChoiceOption": ".chat_completion_tool_choice_option",
    "ChatCompletionToolChoiceOptionZero": ".chat_completion_tool_choice_option_zero",
    "ChatCompletionToolType": ".chat_completion_tool_type",
    "CompletionUsage": ".completion_usage",
    "CreateChatCompletionFunctionResponse": ".create_chat_completion_function_response",
    "CreateChatCompletionFunctionResponseChoicesItem": ".create_chat_completion_function_response_choices_item",
    "CreateChatCompletionFunctionResponseChoicesItemFinishReason": ".create_chat_completion_function_response_choices_item_finish_reason",
    "CreateChatCompletionFunctionResponseObject": ".create_chat_completion_function_response_object",
    "CreateChatCompletionImageResponse": ".create_chat_completion_image_response",
    "CreateChatCompletionResponse": ".create_chat_completion_response",
    "CreateChatCompletionResponseChoicesItem": ".create_chat_completion_response_choices_item",
    "CreateChatCompletionResponseChoicesItemFinishReason": ".create_chat_completion_response_choices_item_finish_reason",
    "CreateChatCompletionResponseChoicesItemLogprobs": ".create_chat_completion_response_choices_item_logprobs",
    "CreateChatCompletionResponseObject": ".create_chat_completion_response_object",
    "CreateChatCompletionStreamResponse": ".create_chat_completion_stream_response",
    "CreateChatCompletionStreamResponseChoicesItem": ".create_chat_completion_stream_response_choices_item",
    "CreateChatCompletionStreamResponseChoicesItemFinishReason": ".create_chat_completion_stream_response_choices_item_finish_reason",
    "CreateChatCompletionStreamResponseChoicesItemLogprobs": ".create_chat_completion_stream_response_choices_item_logprobs",
    "CreateChatCompletionStreamResponseObject": ".create_chat_completion_stream_response_object",
    "CreateCompletionResponse": ".create_completion_response",
    "CreateCompletionResponseChoicesItem": ".create_completion_response_choices_item",
    "CreateCompletionResponseChoicesItemFinishReason": ".create_completion_response_choices_item_finish_reason",
    "CreateCompletionResponseChoicesItemLogprobs": ".create_completion_response_choices_item_logprobs",
    "CreateCompletionResponseObject": ".create_completion_response_object",
    "CreateEmbeddingResponse": ".create_embedding_response",
    "CreateEmbeddingResponseObject": ".create_embedding_response_object",
    "CreateEmbeddingResponseUsage": ".create_embedding_response_usage",
    "CreateMessageRequest": ".create_message_request",
    "CreateMessageRequestRole": ".create_message_request_role",
    "CreateModerationResponse": ".create_moderation_response",
    "CreateModerationResponseResultsItem": ".create_moderation_response_results_item",
    "CreateModerationResponseResultsItemCategories": ".create_moderation_response_results_item_categories",
    "CreateModerationResponseResultsItemCategoryScores": ".create_moderation_response_results_item_category_scores",
    "CreateThreadRequest": ".create_thread_request",
    "CreateTranscriptionResponseJson": ".create_transcription_response_json",
    "CreateTranscriptionResponseVerboseJson": ".create_transcription_response_verbose_json",
    "CreateTranslationResponseJson": ".create_translation_response_json",
    "CreateTranslationResponseVerboseJson": ".create_translation_response_verbose_json",
    "DeleteAssistantFileResponse": ".delete_assistant_file_response",
    "DeleteAssistantFileResponseObject": ".delete_assistant_file_response_object",
    "DeleteAssistantResponse": ".delete_assistant_response",
    "DeleteAssistantResponseObject": ".delete_assistant_response_object",
    "DeleteFileResponse": ".delete_file_response",
    "DeleteFileResponseObject": ".delete_file_response_object",
    "DeleteMessageResponse": ".delete_message_response",
    "DeleteMessageResponseObject": ".delete_message_response_object",
    "DeleteModelResponse": ".delete_model_response",
    "DeleteThreadResponse": ".delete_thread_response",
    "DeleteThreadResponseObject": ".delete_thread_response_object",
    "DoneEvent": ".done_event",
    "DoneEventData": ".done_event_data",
    "DoneEventEvent": ".done_event_event",
    "Embedding": ".embedding",
    "EmbeddingObject": ".embedding_object",
    "Error": ".error",
    "ErrorEvent": ".error_event",
    "ErrorEventEvent": ".error_event_event",
    "ErrorResponse": ".error_response",
    "FineTuningIntegration": ".fine_tuning_integration",
    "FineTuningIntegrationType": ".fine_tuning_integration_type",
    "FineTuningIntegrationWandb": ".fine_tuning_integration_wandb",
    "FineTuningJob": ".fine_tuning_job",
    "FineTuningJobCheckpoint": ".fine_tuning_job_checkpoint",
    "FineTuningJobCheckpointMetrics": ".fine_tuning_job_checkpoint_metrics",
    "FineTuningJobCheckpointObject": ".fine_tuning_job_checkpoint_object",
    "FineTuningJobError": ".fine_tuning_job_error",
    "FineTuningJobEvent": ".fine_tuning_job_event",
    "FineTuningJobEventLevel": ".fine_tuning_job_event_level",
    "FineTuningJobEventObject": ".fine_tuning_job_event_object",
    "FineTuningJobHyperparameters": ".fine_tuning_job_hyperparameters",
    "FineTuningJobHyperparametersNEpochs": ".fine_tuning_job_hyperparameters_n_epochs",
    "FineTuningJobHyperparametersNEpochsZero": ".fine_tuning_job_hyperparameters_n_epochs_zero",
    "FineTuningJobObject": ".fine_tuning_job_object",
    "FineTuningJobStatus": ".fine_tuning_job_status",
    "FunctionObject": ".function_object",
    "FunctionParameters": ".function_parameters",
    "Image": ".image",
    "ImagesResponse": ".images_response",
    "ListAssistantFilesResponse": ".list_assistant_files_response",
    "ListAssistantsResponse": ".list_assistants_response",
    "ListFilesResponse": ".list_files_response",
    "ListFilesResponseObject": ".list_files_response_object",
    "ListFineTuningJobCheckpointsResponse": ".list_fine_tuning_job_checkpoints_response",
    "ListFineTuningJobCheckpointsResponseObject": ".list_fine_tuning_job_checkpoints_response_object",
    "ListFineTuningJobEventsResponse": ".list_fine_tuning_job_events_response",
    "ListFineTuningJobEventsResponseObject": ".list_fine_tuning_job_events_response_object",
    "ListMessageFilesResponse": ".list_message_files_response",
    "ListMessagesResponse": ".list_messages_response",
    "ListModelsResponse": ".list_models_response",
    "ListModelsResponseObject": ".list_models_response_object",
    "ListPaginatedFineTuningJobsResponse": ".list_paginated_fine_tuning_jobs_response",
    "ListPaginatedFineTuningJobsResponseObject": ".list_paginated_fine_tuning_jobs_response_object",
    "ListRunStepsResponse": ".list_run_steps_response",
    "ListRunsResponse": ".list_runs_response",
    "ListThreadsResponse": ".list_threads_response",
    "MessageContentImageFileObject": ".message_content_image_file_object",
    "MessageContentImageFileObjectImageFile": ".message_content_image_file_object_image_file",
    "MessageContentTextAnnotationsFileCitationObject": ".message_content_text_annotations_file_citation_object",
    "MessageContentTextAnnotationsFileCitationObjectFileCitation": ".message_content_text_annotations_file_citation_object_file_citation",
    "MessageContentTextAnnotationsFilePathObject": ".message_content_text_annotations_file_path_object",
    "MessageContentTextAnnotationsFilePathObjectFilePath": ".message_content_text_annotations_file_path_object_file_path",
    "MessageContentTextObject": ".message_content_text_object",
    "MessageContentTextObjectText": ".message_content_text_object_text",
    "MessageContentTextObjectTextAnnotationsItem": ".message_content_text_object_text_annotations_item",
    "MessageContentTextObjectTextAnnotationsItem_FileCitation": ".message_content_text_object_text_annotations_item",
    "MessageContentTextObjectTextAnnotationsItem_FilePath": ".message_content_text_object_text_annotations_item",
    "MessageDeltaContentImageFileObject": ".message_delta_content_image_file_object",
    "MessageDeltaContentImageFileObjectImageFile": ".message_delta_content_image_file_object_image_file",
    "MessageDeltaContentTextAnnotationsFileCitationObject": ".message_delta_content_text_annotations_file_citation_object",
    "MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation": ".message_delta_content_text_annotations_file_citation_object_file_citation",
    "MessageDeltaContentTextAnnotationsFilePathObject": ".message_delta_content_text_annotations_file_path_object",
    "MessageDeltaContentTextAnnotationsFilePathObjectFilePath": ".message_delta_content_text_annotations_file_path_object_file_path",
    "MessageDeltaContentTextObject": ".message_delta_content_text_object",
    "MessageDeltaContentTextObjectText": ".message_delta_content_text_object_text",
    "MessageDeltaContentTextObjectTextAnnotationsItem": ".message_delta_content_text_object_text_annotations_item",
    "MessageDeltaContentTextObjectTextAnnotationsItem_FileCitation": ".message_delta_content_text_object_text_annotations_item",
    "MessageDeltaContentTextObjectTextAnnotationsItem_FilePath": ".message_delta_content_text_object_text_annotations_item",
    "MessageDeltaObject": ".message_delta_object",
    "MessageDeltaObjectDelta": ".message_delta_object_delta",
    "MessageDeltaObjectDeltaContentItem": ".message_delta_object_delta_content_item",
    "MessageDeltaObjectDeltaContentItem_ImageFile": ".message_delta_object_delta_content_item",
    "MessageDeltaObjectDeltaContentItem_Text": ".message_delta_object_delta_content_item",
    "MessageDeltaObjectDeltaRole": ".message_delta_object_delta_role",
    "MessageDeltaObjectObject": ".message_delta_object_object",
    "MessageFileObject": ".message_file_object",
    "MessageFileObjectObject": ".message_file_object_object",
    "MessageObject": ".message_object",
    "MessageObjectContentItem": ".message_object_content_item",
    "MessageObjectContentItem_ImageFile": ".message_object_content_item",
    "MessageObjectContentItem_Text": ".message_object_content_item",
    "MessageObjectIncompleteDetails": ".message_object_incomplete_details",
    "MessageObjectIncompleteDetailsReason": ".message_object_incomplete_details_reason",
    "MessageObjectObject": ".message_object_object",
    "MessageObjectRole": ".message_object_role",
    "MessageObjectStatus": ".message_object_status",
    "MessageStreamEvent": ".message_stream_event",
    "MessageStreamEventThreadMessageCompleted": ".message_stream_event_thread_message_completed",
    "MessageStreamEventThreadMessageCreated": ".message_stream_event_thread_message_created",
    "MessageStreamEventThreadMessageDelta": ".message_stream_event_thread_message_delta",
    "MessageStreamEventThreadMessageInProgress": ".message_stream_event_thread_message_in_progress",
    "MessageStreamEventThreadMessageIncomplete": ".message_stream_event_thread_message_incomplete",
    "MessageStreamEvent_ThreadMessageCompleted": ".message_stream_event",
    "MessageStreamEvent_ThreadMessageCreated": ".message_stream_event",
    "MessageStreamEvent_ThreadMessageDelta": ".message_stream_event",
    "MessageStreamEvent_ThreadMessageInProgress": ".message_stream_event",
    "MessageStreamEvent_ThreadMessageIncomplete": ".message_stream_event",
    "Model": ".model",
    "ModelObject": ".model_object",
    "OpenAiFile": ".open_ai_file",
    "OpenAiFileObject": ".open_ai_file_object",
    "OpenAiFilePurpose": ".open_ai_file_purpose",
    "OpenAiFileStatus": ".open_ai_file_status",
    "RunCompletionUsage": ".run_completion_usage",
    "RunObject": ".run_object",
    "RunObjectIncompleteDetails": ".run_object_incomplete_details",
    "RunObjectIncompleteDetailsReason": ".run_object_incomplete_details_reason",
    "RunObjectLastError": ".run_object_last_error",
    "RunObjectLastErrorCode": ".run_object_last_error_code",
    "RunObjectObject": ".run_object_object",
    "RunObjectRequiredAction": ".run_object_required_action",
    "RunObjectRequiredActionSubmitToolOutputs": ".run_object_required_action_submit_tool_outputs",
    "RunObjectRequiredActionType": ".run_object_required_action_type",
    "RunObjectStatus": ".run_object_status",
    "RunObjectToolsItem": ".run_object_tools_item",
    "RunObjectToolsItem_CodeInterpreter": ".run_object_tools_item",
    "RunObjectToolsItem_Function": ".run_object_tools_item",
    "RunObjectToolsItem_Retrieval": ".run_object_tools_item",
    "RunStepCompletionUsage": ".run_step_completion_usage",
    "RunStepDeltaObject": ".run_step_delta_object",
    "RunStepDeltaObjectDelta": ".run_step_delta_object_delta",
    "RunStepDeltaObjectDeltaStepDetails": ".run_step_delta_object_delta_step_details",
    "RunStepDeltaObjectDeltaStepDetails_MessageCreation": ".run_step_delta_object_delta_step_details",
    "RunStepDeltaObjectDeltaStepDetails_ToolCalls": ".run_step_delta_object_delta_step_details",
    "RunStepDeltaObjectObject": ".run_step_delta_object_object",
    "RunStepDeltaStepDetailsMessageCreationObject": ".run_step_delta_step_details_message_creation_object",
    "RunStepDeltaStepDetailsMessageCreationObjectMessageCreation": ".run_step_delta_step_details_message_creation_object_message_creation",
    "RunStepDeltaStepDetailsToolCallsCodeObject": ".run_step_delta_step_details_tool_calls_code_object",
    "RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter": ".run_step_delta_step_details_tool_calls_code_object_code_interpreter",
    "RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem": ".run_step_delta_step_details_tool_calls_code_object_code_interpreter_outputs_item",
    "RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image": ".run_step_delta_step_details_tool_calls_code_object_code_interpreter_outputs_item",
    "RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs": ".run_step_delta_step_details_tool_calls_code_object_code_interpreter_outputs_item",
    "RunStepDeltaStepDetailsToolCallsCodeOutputImageObject": ".run_step_delta_step_details_tool_calls_code_output_image_object",
    "RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage": ".run_step_delta_step_details_tool_calls_code_output_image_object_image",
    "RunStepDeltaStepDetailsToolCallsCodeOutputLogsObject": ".run_step_delta_step_details_tool_calls_code_output_logs_object",
    "RunStepDeltaStepDetailsToolCallsFunctionObject": ".run_step_delta_step_details_tool_calls_function_object",
    "RunStepDeltaStepDetailsToolCallsFunctionObjectFunction": ".run_step_delta_step_details_tool_calls_function_object_function",
    "RunStepDeltaStepDetailsToolCallsObject": ".run_step_delta_step_details_tool_calls_object",
    "RunStepDeltaStepDetailsToolCallsObjectToolCallsItem": ".run_step_delta_step_details_tool_calls_object_tool_calls_item",
    "RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter": ".run_step_delta_step_details_tool_calls_object_tool_calls_item",
    "RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Function": ".run_step_delta_step_details_tool_calls_object_tool_calls_item",
    "RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Retrieval": ".run_step_delta_step_details_tool_calls_object_tool_calls_item",
    "RunStepDeltaStepDetailsToolCallsRetrievalObject": ".run_step_delta_step_details_tool_calls_retrieval_object",
    "RunStepDetailsMessageCreationObject": ".run_step_details_message_creation_object",
    "RunStepDetailsMessageCreationObjectMessageCreation": ".run_step_details_message_creation_object_message_creation",
    "RunStepDetailsToolCallsCodeObject": ".run_step_details_tool_calls_code_object",
    "RunStepDetailsToolCallsCodeObjectCodeInterpreter": ".run_step_details_tool_calls_code_object_code_interpreter",
    "RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem": ".run_step_details_tool_calls_code_object_code_interpreter_outputs_item",
    "RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image": ".run_step_details_tool_calls_code_object_code_interpreter_outputs_item",
    "RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs": ".run_step_details_tool_calls_code_object_code_interpreter_outputs_item",
    "RunStepDetailsToolCallsCodeOutputImageObject": ".run_step_details_tool_calls_code_output_image_object",
    "RunStepDetailsToolCallsCodeOutputImageObjectImage": ".run_step_details_tool_calls_code_output_image_object_image",
    "RunStepDetailsToolCallsCodeOutputLogsObject": ".run_step_details_tool_calls_code_output_logs_object",
    "RunStepDetailsToolCallsFunctionObject": ".run_step_details_tool_calls_function_object",
    "RunStepDetailsToolCallsFunctionObjectFunction": ".run_step_details_tool_calls_function_object_function",
    "RunStepDetailsToolCallsObject": ".run_step_details_tool_calls_object",
    "RunStepDetailsToolCallsObjectToolCallsItem": ".run_step_details_tool_calls_object_tool_calls_item",
    "RunStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter": ".run_step_details_tool_calls_object_tool_calls_item",
    "RunStepDetailsToolCallsObjectToolCallsItem_Function": ".run_step_details_tool_calls_object_tool_calls_item",
    "RunStepDetailsToolCallsObjectToolCallsItem_Retrieval": ".run_step_details_tool_calls_object_tool_calls_item",
    "RunStepDetailsToolCallsRetrievalObject": ".run_step_details_tool_calls_retrieval_object",
    "RunStepObject": ".run_step_object",
    "RunStepObjectLastError": ".run_step_object_last_error",
    "RunStepObjectLastErrorCode": ".run_step_object_last_error_code",
    "RunStepObjectObject": ".run_step_object_object",
    "RunStepObjectStatus": ".run_step_object_status",
    "RunStepObjectStepDetails": ".run_step_object_step_details",
    "RunStepObjectStepDetails_MessageCreation": ".run_step_object_step_details",
    "RunStepObjectStepDetails_ToolCalls": ".run_step_object_step_details",
    "RunStepObjectType": ".run_step_object_type",
    "RunStepStreamEvent": ".run_step_stream_event",
    "RunStepStreamEventThreadRunStepCancelled": ".run_step_stream_event_thread_run_step_cancelled",
    "RunStepStreamEventThreadRunStepCompleted": ".run_step_stream_event_thread_run_step_completed",
    "RunStepStreamEventThreadRunStepCreated": ".run_step_stream_event_thread_run_step_created",
    "RunStepStreamEventThreadRunStepDelta": ".run_step_stream_event_thread_run_step_delta",
    "RunStepStreamEventThreadRunStepExpired": ".run_step_stream_event_thread_run_step_expired",
    "RunStepStreamEventThreadRunStepFailed": ".run_step_stream_event_thread_run_step_failed",
    "RunStepStreamEventThreadRunStepInProgress": ".run_step_stream_event_thread_run_step_in_progress",
    "RunStepStreamEvent_ThreadRunStepCancelled": ".run_step_stream_event",
    "RunStepStreamEvent_ThreadRunStepCompleted": ".run_step_stream_event",
    "RunStepStreamEvent_ThreadRunStepCreated": ".run_step_stream_event",
    "RunStepStreamEvent_ThreadRunStepDelta": ".run_step_stream_event",
    "RunStepStreamEvent_ThreadRunStepExpired": ".run_step_stream_event",
    "RunStepStreamEvent_ThreadRunStepFailed": ".run_step_stream_event",
    "RunStepStreamEvent_ThreadRunStepInProgress": ".run_step_stream_event",
    "RunStreamEvent": ".run_stream_event",
    "RunStreamEventThreadRunCancelled": ".run_stream_event_thread_run_cancelled",
    "RunStreamEventThreadRunCancelling": ".run_stream_event_thread_run_cancelling",
    "RunStreamEventThreadRunCompleted": ".run_stream_event_thread_run_completed",
    "RunStreamEventThreadRunCreated": ".run_stream_event_thread_run_created",
    "RunStreamEventThreadRunExpired": ".run_stream_event_thread_run_expired",
    "RunStreamEventThreadRunFailed": ".run_stream_event_thread_run_failed",
    "RunStreamEventThreadRunInProgress": ".run_stream_event_thread_run_in_progress",
    "RunStreamEventThreadRunQueued": ".run_stream_event_thread_run_queued",
    "RunStreamEventThreadRunRequiresAction": ".run_stream_event_thread_run_requires_action",
    "RunStreamEvent_ThreadRunCancelled": ".run_stream_event",
    "RunStreamEvent_ThreadRunCancelling": ".run_stream_event",
    "RunStreamEvent_ThreadRunCompleted": ".run_stream_event",
    "RunStreamEvent_ThreadRunCreated": ".run_stream_event",
    "RunStreamEvent_ThreadRunExpired": ".run_stream_event",
    "RunStreamEvent_ThreadRunFailed": ".run_stream_event",
    "RunStreamEvent_ThreadRunInProgress": ".run_stream_event",
    "RunStreamEvent_ThreadRunQueued": ".run_stream_event",
    "RunStreamEvent_ThreadRunRequiresAction": ".run_stream_event",
    "RunToolCallObject": ".run_tool_call_object",
    "RunToolCallObjectFunction": ".run_tool_call_object_function",
    "RunToolCallObjectType": ".run_tool_call_object_type",
    "ThreadObject": ".thread_object",
    "ThreadObjectObject": ".thread_object_object",
    "ThreadStreamEvent": ".thread_stream_event",
    "ThreadStreamEventEvent": ".thread_stream_event_event",
    "TranscriptionSegment": ".transcription_segment",
    "TranscriptionWord": ".transcription_word",
    "TruncationObject": ".truncation_object",
    "TruncationObjectType": ".truncation_object_type",
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
    "AssistantFileObject",
    "AssistantFileObjectObject",
    "AssistantObject",
    "AssistantObjectObject",
    "AssistantObjectToolsItem",
    "AssistantObjectToolsItem_CodeInterpreter",
    "AssistantObjectToolsItem_Function",
    "AssistantObjectToolsItem_Retrieval",
    "AssistantStreamEvent",
    "AssistantToolsCode",
    "AssistantToolsFunction",
    "AssistantToolsRetrieval",
    "AssistantsApiNamedToolChoice",
    "AssistantsApiNamedToolChoiceFunction",
    "AssistantsApiNamedToolChoiceType",
    "AssistantsApiResponseFormat",
    "AssistantsApiResponseFormatOption",
    "AssistantsApiResponseFormatOptionZero",
    "AssistantsApiResponseFormatType",
    "AssistantsApiToolChoiceOption",
    "AssistantsApiToolChoiceOptionZero",
    "ChatCompletionFunctionCallOption",
    "ChatCompletionFunctions",
    "ChatCompletionMessageToolCall",
    "ChatCompletionMessageToolCallChunk",
    "ChatCompletionMessageToolCallChunkFunction",
    "ChatCompletionMessageToolCallChunkType",
    "ChatCompletionMessageToolCallFunction",
    "ChatCompletionMessageToolCallType",
    "ChatCompletionMessageToolCalls",
    "ChatCompletionNamedToolChoice",
    "ChatCompletionNamedToolChoiceFunction",
    "ChatCompletionNamedToolChoiceType",
    "ChatCompletionRequestAssistantMessage",
    "ChatCompletionRequestAssistantMessageFunctionCall",
    "ChatCompletionRequestFunctionMessage",
    "ChatCompletionRequestMessage",
    "ChatCompletionRequestMessageContentPart",
    "ChatCompletionRequestMessageContentPartImage",
    "ChatCompletionRequestMessageContentPartImageImageUrl",
    "ChatCompletionRequestMessageContentPartImageImageUrlDetail",
    "ChatCompletionRequestMessageContentPartText",
    "ChatCompletionRequestMessageContentPart_ImageUrl",
    "ChatCompletionRequestMessageContentPart_Text",
    "ChatCompletionRequestMessage_Assistant",
    "ChatCompletionRequestMessage_Function",
    "ChatCompletionRequestMessage_System",
    "ChatCompletionRequestMessage_Tool",
    "ChatCompletionRequestMessage_User",
    "ChatCompletionRequestSystemMessage",
    "ChatCompletionRequestToolMessage",
    "ChatCompletionRequestUserMessage",
    "ChatCompletionRequestUserMessageContent",
    "ChatCompletionResponseMessage",
    "ChatCompletionResponseMessageFunctionCall",
    "ChatCompletionResponseMessageRole",
    "ChatCompletionRole",
    "ChatCompletionStreamResponseDelta",
    "ChatCompletionStreamResponseDeltaFunctionCall",
    "ChatCompletionStreamResponseDeltaRole",
    "ChatCompletionTokenLogprob",
    "ChatCompletionTokenLogprobTopLogprobsItem",
    "ChatCompletionTool",
    "ChatCompletionToolChoiceOption",
    "ChatCompletionToolChoiceOptionZero",
    "ChatCompletionToolType",
    "CompletionUsage",
    "CreateChatCompletionFunctionResponse",
    "CreateChatCompletionFunctionResponseChoicesItem",
    "CreateChatCompletionFunctionResponseChoicesItemFinishReason",
    "CreateChatCompletionFunctionResponseObject",
    "CreateChatCompletionImageResponse",
    "CreateChatCompletionResponse",
    "CreateChatCompletionResponseChoicesItem",
    "CreateChatCompletionResponseChoicesItemFinishReason",
    "CreateChatCompletionResponseChoicesItemLogprobs",
    "CreateChatCompletionResponseObject",
    "CreateChatCompletionStreamResponse",
    "CreateChatCompletionStreamResponseChoicesItem",
    "CreateChatCompletionStreamResponseChoicesItemFinishReason",
    "CreateChatCompletionStreamResponseChoicesItemLogprobs",
    "CreateChatCompletionStreamResponseObject",
    "CreateCompletionResponse",
    "CreateCompletionResponseChoicesItem",
    "CreateCompletionResponseChoicesItemFinishReason",
    "CreateCompletionResponseChoicesItemLogprobs",
    "CreateCompletionResponseObject",
    "CreateEmbeddingResponse",
    "CreateEmbeddingResponseObject",
    "CreateEmbeddingResponseUsage",
    "CreateMessageRequest",
    "CreateMessageRequestRole",
    "CreateModerationResponse",
    "CreateModerationResponseResultsItem",
    "CreateModerationResponseResultsItemCategories",
    "CreateModerationResponseResultsItemCategoryScores",
    "CreateThreadRequest",
    "CreateTranscriptionResponseJson",
    "CreateTranscriptionResponseVerboseJson",
    "CreateTranslationResponseJson",
    "CreateTranslationResponseVerboseJson",
    "DeleteAssistantFileResponse",
    "DeleteAssistantFileResponseObject",
    "DeleteAssistantResponse",
    "DeleteAssistantResponseObject",
    "DeleteFileResponse",
    "DeleteFileResponseObject",
    "DeleteMessageResponse",
    "DeleteMessageResponseObject",
    "DeleteModelResponse",
    "DeleteThreadResponse",
    "DeleteThreadResponseObject",
    "DoneEvent",
    "DoneEventData",
    "DoneEventEvent",
    "Embedding",
    "EmbeddingObject",
    "Error",
    "ErrorEvent",
    "ErrorEventEvent",
    "ErrorResponse",
    "FineTuningIntegration",
    "FineTuningIntegrationType",
    "FineTuningIntegrationWandb",
    "FineTuningJob",
    "FineTuningJobCheckpoint",
    "FineTuningJobCheckpointMetrics",
    "FineTuningJobCheckpointObject",
    "FineTuningJobError",
    "FineTuningJobEvent",
    "FineTuningJobEventLevel",
    "FineTuningJobEventObject",
    "FineTuningJobHyperparameters",
    "FineTuningJobHyperparametersNEpochs",
    "FineTuningJobHyperparametersNEpochsZero",
    "FineTuningJobObject",
    "FineTuningJobStatus",
    "FunctionObject",
    "FunctionParameters",
    "Image",
    "ImagesResponse",
    "ListAssistantFilesResponse",
    "ListAssistantsResponse",
    "ListFilesResponse",
    "ListFilesResponseObject",
    "ListFineTuningJobCheckpointsResponse",
    "ListFineTuningJobCheckpointsResponseObject",
    "ListFineTuningJobEventsResponse",
    "ListFineTuningJobEventsResponseObject",
    "ListMessageFilesResponse",
    "ListMessagesResponse",
    "ListModelsResponse",
    "ListModelsResponseObject",
    "ListPaginatedFineTuningJobsResponse",
    "ListPaginatedFineTuningJobsResponseObject",
    "ListRunStepsResponse",
    "ListRunsResponse",
    "ListThreadsResponse",
    "MessageContentImageFileObject",
    "MessageContentImageFileObjectImageFile",
    "MessageContentTextAnnotationsFileCitationObject",
    "MessageContentTextAnnotationsFileCitationObjectFileCitation",
    "MessageContentTextAnnotationsFilePathObject",
    "MessageContentTextAnnotationsFilePathObjectFilePath",
    "MessageContentTextObject",
    "MessageContentTextObjectText",
    "MessageContentTextObjectTextAnnotationsItem",
    "MessageContentTextObjectTextAnnotationsItem_FileCitation",
    "MessageContentTextObjectTextAnnotationsItem_FilePath",
    "MessageDeltaContentImageFileObject",
    "MessageDeltaContentImageFileObjectImageFile",
    "MessageDeltaContentTextAnnotationsFileCitationObject",
    "MessageDeltaContentTextAnnotationsFileCitationObjectFileCitation",
    "MessageDeltaContentTextAnnotationsFilePathObject",
    "MessageDeltaContentTextAnnotationsFilePathObjectFilePath",
    "MessageDeltaContentTextObject",
    "MessageDeltaContentTextObjectText",
    "MessageDeltaContentTextObjectTextAnnotationsItem",
    "MessageDeltaContentTextObjectTextAnnotationsItem_FileCitation",
    "MessageDeltaContentTextObjectTextAnnotationsItem_FilePath",
    "MessageDeltaObject",
    "MessageDeltaObjectDelta",
    "MessageDeltaObjectDeltaContentItem",
    "MessageDeltaObjectDeltaContentItem_ImageFile",
    "MessageDeltaObjectDeltaContentItem_Text",
    "MessageDeltaObjectDeltaRole",
    "MessageDeltaObjectObject",
    "MessageFileObject",
    "MessageFileObjectObject",
    "MessageObject",
    "MessageObjectContentItem",
    "MessageObjectContentItem_ImageFile",
    "MessageObjectContentItem_Text",
    "MessageObjectIncompleteDetails",
    "MessageObjectIncompleteDetailsReason",
    "MessageObjectObject",
    "MessageObjectRole",
    "MessageObjectStatus",
    "MessageStreamEvent",
    "MessageStreamEventThreadMessageCompleted",
    "MessageStreamEventThreadMessageCreated",
    "MessageStreamEventThreadMessageDelta",
    "MessageStreamEventThreadMessageInProgress",
    "MessageStreamEventThreadMessageIncomplete",
    "MessageStreamEvent_ThreadMessageCompleted",
    "MessageStreamEvent_ThreadMessageCreated",
    "MessageStreamEvent_ThreadMessageDelta",
    "MessageStreamEvent_ThreadMessageInProgress",
    "MessageStreamEvent_ThreadMessageIncomplete",
    "Model",
    "ModelObject",
    "OpenAiFile",
    "OpenAiFileObject",
    "OpenAiFilePurpose",
    "OpenAiFileStatus",
    "RunCompletionUsage",
    "RunObject",
    "RunObjectIncompleteDetails",
    "RunObjectIncompleteDetailsReason",
    "RunObjectLastError",
    "RunObjectLastErrorCode",
    "RunObjectObject",
    "RunObjectRequiredAction",
    "RunObjectRequiredActionSubmitToolOutputs",
    "RunObjectRequiredActionType",
    "RunObjectStatus",
    "RunObjectToolsItem",
    "RunObjectToolsItem_CodeInterpreter",
    "RunObjectToolsItem_Function",
    "RunObjectToolsItem_Retrieval",
    "RunStepCompletionUsage",
    "RunStepDeltaObject",
    "RunStepDeltaObjectDelta",
    "RunStepDeltaObjectDeltaStepDetails",
    "RunStepDeltaObjectDeltaStepDetails_MessageCreation",
    "RunStepDeltaObjectDeltaStepDetails_ToolCalls",
    "RunStepDeltaObjectObject",
    "RunStepDeltaStepDetailsMessageCreationObject",
    "RunStepDeltaStepDetailsMessageCreationObjectMessageCreation",
    "RunStepDeltaStepDetailsToolCallsCodeObject",
    "RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter",
    "RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem",
    "RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image",
    "RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs",
    "RunStepDeltaStepDetailsToolCallsCodeOutputImageObject",
    "RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage",
    "RunStepDeltaStepDetailsToolCallsCodeOutputLogsObject",
    "RunStepDeltaStepDetailsToolCallsFunctionObject",
    "RunStepDeltaStepDetailsToolCallsFunctionObjectFunction",
    "RunStepDeltaStepDetailsToolCallsObject",
    "RunStepDeltaStepDetailsToolCallsObjectToolCallsItem",
    "RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter",
    "RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Function",
    "RunStepDeltaStepDetailsToolCallsObjectToolCallsItem_Retrieval",
    "RunStepDeltaStepDetailsToolCallsRetrievalObject",
    "RunStepDetailsMessageCreationObject",
    "RunStepDetailsMessageCreationObjectMessageCreation",
    "RunStepDetailsToolCallsCodeObject",
    "RunStepDetailsToolCallsCodeObjectCodeInterpreter",
    "RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem",
    "RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Image",
    "RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem_Logs",
    "RunStepDetailsToolCallsCodeOutputImageObject",
    "RunStepDetailsToolCallsCodeOutputImageObjectImage",
    "RunStepDetailsToolCallsCodeOutputLogsObject",
    "RunStepDetailsToolCallsFunctionObject",
    "RunStepDetailsToolCallsFunctionObjectFunction",
    "RunStepDetailsToolCallsObject",
    "RunStepDetailsToolCallsObjectToolCallsItem",
    "RunStepDetailsToolCallsObjectToolCallsItem_CodeInterpreter",
    "RunStepDetailsToolCallsObjectToolCallsItem_Function",
    "RunStepDetailsToolCallsObjectToolCallsItem_Retrieval",
    "RunStepDetailsToolCallsRetrievalObject",
    "RunStepObject",
    "RunStepObjectLastError",
    "RunStepObjectLastErrorCode",
    "RunStepObjectObject",
    "RunStepObjectStatus",
    "RunStepObjectStepDetails",
    "RunStepObjectStepDetails_MessageCreation",
    "RunStepObjectStepDetails_ToolCalls",
    "RunStepObjectType",
    "RunStepStreamEvent",
    "RunStepStreamEventThreadRunStepCancelled",
    "RunStepStreamEventThreadRunStepCompleted",
    "RunStepStreamEventThreadRunStepCreated",
    "RunStepStreamEventThreadRunStepDelta",
    "RunStepStreamEventThreadRunStepExpired",
    "RunStepStreamEventThreadRunStepFailed",
    "RunStepStreamEventThreadRunStepInProgress",
    "RunStepStreamEvent_ThreadRunStepCancelled",
    "RunStepStreamEvent_ThreadRunStepCompleted",
    "RunStepStreamEvent_ThreadRunStepCreated",
    "RunStepStreamEvent_ThreadRunStepDelta",
    "RunStepStreamEvent_ThreadRunStepExpired",
    "RunStepStreamEvent_ThreadRunStepFailed",
    "RunStepStreamEvent_ThreadRunStepInProgress",
    "RunStreamEvent",
    "RunStreamEventThreadRunCancelled",
    "RunStreamEventThreadRunCancelling",
    "RunStreamEventThreadRunCompleted",
    "RunStreamEventThreadRunCreated",
    "RunStreamEventThreadRunExpired",
    "RunStreamEventThreadRunFailed",
    "RunStreamEventThreadRunInProgress",
    "RunStreamEventThreadRunQueued",
    "RunStreamEventThreadRunRequiresAction",
    "RunStreamEvent_ThreadRunCancelled",
    "RunStreamEvent_ThreadRunCancelling",
    "RunStreamEvent_ThreadRunCompleted",
    "RunStreamEvent_ThreadRunCreated",
    "RunStreamEvent_ThreadRunExpired",
    "RunStreamEvent_ThreadRunFailed",
    "RunStreamEvent_ThreadRunInProgress",
    "RunStreamEvent_ThreadRunQueued",
    "RunStreamEvent_ThreadRunRequiresAction",
    "RunToolCallObject",
    "RunToolCallObjectFunction",
    "RunToolCallObjectType",
    "ThreadObject",
    "ThreadObjectObject",
    "ThreadStreamEvent",
    "ThreadStreamEventEvent",
    "TranscriptionSegment",
    "TranscriptionWord",
    "TruncationObject",
    "TruncationObjectType",
]
