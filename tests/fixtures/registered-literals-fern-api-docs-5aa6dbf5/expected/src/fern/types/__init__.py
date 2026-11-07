



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .analyze_commit_diff_response import AnalyzeCommitDiffResponse
    from .chat_message import ChatMessage
    from .chat_message_role import ChatMessageRole
    from .chat_source import ChatSource
    from .code import Code
    from .conversation import Conversation
    from .conversation_turn import ConversationTurn
    from .conversation_turn_feedback import ConversationTurnFeedback
    from .create_code_record_response import CreateCodeRecordResponse
    from .create_document_response import CreateDocumentResponse
    from .create_feedback_response import CreateFeedbackResponse
    from .create_guidance_response import CreateGuidanceResponse
    from .create_query_response import CreateQueryResponse
    from .delete_all_websites_response import DeleteAllWebsitesResponse
    from .delete_code_record_response import DeleteCodeRecordResponse
    from .delete_document_request import DeleteDocumentRequest
    from .delete_document_response import DeleteDocumentResponse
    from .delete_documents_response import DeleteDocumentsResponse
    from .delete_guidance_response import DeleteGuidanceResponse
    from .delete_website_response import DeleteWebsiteResponse
    from .document import Document
    from .enable_ask_ai_response import EnableAskAiResponse
    from .feedback import Feedback
    from .get_code_record_response import GetCodeRecordResponse
    from .get_code_records_response import GetCodeRecordsResponse
    from .get_conversation_resolution_response import GetConversationResolutionResponse
    from .get_conversation_response import GetConversationResponse
    from .get_document_response import GetDocumentResponse
    from .get_documents_response import GetDocumentsResponse
    from .get_feedback_response import GetFeedbackResponse
    from .get_guidance_response import GetGuidanceResponse
    from .get_guidances_response import GetGuidancesResponse
    from .get_histogram_analytics_response import GetHistogramAnalyticsResponse
    from .get_insights_response import GetInsightsResponse
    from .get_mcp_bmf_query_response import GetMcpBmfQueryResponse
    from .get_mcp_semantic_query_response import GetMcpSemanticQueryResponse
    from .get_queries_response import GetQueriesResponse
    from .get_settings_response import GetSettingsResponse
    from .get_website_response import GetWebsiteResponse
    from .get_website_status_response import GetWebsiteStatusResponse
    from .get_websites_response import GetWebsitesResponse
    from .group_by import GroupBy
    from .guidance import Guidance
    from .histogram_analytics_bar import HistogramAnalyticsBar
    from .http_validation_error import HttpValidationError
    from .index_website_response import IndexWebsiteResponse
    from .insight_example import InsightExample
    from .insight_with_metadata import InsightWithMetadata
    from .job_status_response import JobStatusResponse
    from .language_model import LanguageModel
    from .pagination_response import PaginationResponse
    from .post_chat_completion_response import PostChatCompletionResponse
    from .query import Query
    from .query_status import QueryStatus
    from .reconstruct_index_response import ReconstructIndexResponse
    from .reindex_website_response import ReindexWebsiteResponse
    from .reindexing_job_record import ReindexingJobRecord
    from .resolution_filter import ResolutionFilter
    from .sync_index_response import SyncIndexResponse
    from .toggle_ask_ai_response import ToggleAskAiResponse
    from .toggle_status_response import ToggleStatusResponse
    from .update_document_response import UpdateDocumentResponse
    from .update_guidance_response import UpdateGuidanceResponse
    from .update_reindexing_job_status_response import UpdateReindexingJobStatusResponse
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .version_bump import VersionBump
    from .website import Website
_dynamic_imports: typing.Dict[str, str] = {
    "AnalyzeCommitDiffResponse": ".analyze_commit_diff_response",
    "ChatMessage": ".chat_message",
    "ChatMessageRole": ".chat_message_role",
    "ChatSource": ".chat_source",
    "Code": ".code",
    "Conversation": ".conversation",
    "ConversationTurn": ".conversation_turn",
    "ConversationTurnFeedback": ".conversation_turn_feedback",
    "CreateCodeRecordResponse": ".create_code_record_response",
    "CreateDocumentResponse": ".create_document_response",
    "CreateFeedbackResponse": ".create_feedback_response",
    "CreateGuidanceResponse": ".create_guidance_response",
    "CreateQueryResponse": ".create_query_response",
    "DeleteAllWebsitesResponse": ".delete_all_websites_response",
    "DeleteCodeRecordResponse": ".delete_code_record_response",
    "DeleteDocumentRequest": ".delete_document_request",
    "DeleteDocumentResponse": ".delete_document_response",
    "DeleteDocumentsResponse": ".delete_documents_response",
    "DeleteGuidanceResponse": ".delete_guidance_response",
    "DeleteWebsiteResponse": ".delete_website_response",
    "Document": ".document",
    "EnableAskAiResponse": ".enable_ask_ai_response",
    "Feedback": ".feedback",
    "GetCodeRecordResponse": ".get_code_record_response",
    "GetCodeRecordsResponse": ".get_code_records_response",
    "GetConversationResolutionResponse": ".get_conversation_resolution_response",
    "GetConversationResponse": ".get_conversation_response",
    "GetDocumentResponse": ".get_document_response",
    "GetDocumentsResponse": ".get_documents_response",
    "GetFeedbackResponse": ".get_feedback_response",
    "GetGuidanceResponse": ".get_guidance_response",
    "GetGuidancesResponse": ".get_guidances_response",
    "GetHistogramAnalyticsResponse": ".get_histogram_analytics_response",
    "GetInsightsResponse": ".get_insights_response",
    "GetMcpBmfQueryResponse": ".get_mcp_bmf_query_response",
    "GetMcpSemanticQueryResponse": ".get_mcp_semantic_query_response",
    "GetQueriesResponse": ".get_queries_response",
    "GetSettingsResponse": ".get_settings_response",
    "GetWebsiteResponse": ".get_website_response",
    "GetWebsiteStatusResponse": ".get_website_status_response",
    "GetWebsitesResponse": ".get_websites_response",
    "GroupBy": ".group_by",
    "Guidance": ".guidance",
    "HistogramAnalyticsBar": ".histogram_analytics_bar",
    "HttpValidationError": ".http_validation_error",
    "IndexWebsiteResponse": ".index_website_response",
    "InsightExample": ".insight_example",
    "InsightWithMetadata": ".insight_with_metadata",
    "JobStatusResponse": ".job_status_response",
    "LanguageModel": ".language_model",
    "PaginationResponse": ".pagination_response",
    "PostChatCompletionResponse": ".post_chat_completion_response",
    "Query": ".query",
    "QueryStatus": ".query_status",
    "ReconstructIndexResponse": ".reconstruct_index_response",
    "ReindexWebsiteResponse": ".reindex_website_response",
    "ReindexingJobRecord": ".reindexing_job_record",
    "ResolutionFilter": ".resolution_filter",
    "SyncIndexResponse": ".sync_index_response",
    "ToggleAskAiResponse": ".toggle_ask_ai_response",
    "ToggleStatusResponse": ".toggle_status_response",
    "UpdateDocumentResponse": ".update_document_response",
    "UpdateGuidanceResponse": ".update_guidance_response",
    "UpdateReindexingJobStatusResponse": ".update_reindexing_job_status_response",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VersionBump": ".version_bump",
    "Website": ".website",
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
    "AnalyzeCommitDiffResponse",
    "ChatMessage",
    "ChatMessageRole",
    "ChatSource",
    "Code",
    "Conversation",
    "ConversationTurn",
    "ConversationTurnFeedback",
    "CreateCodeRecordResponse",
    "CreateDocumentResponse",
    "CreateFeedbackResponse",
    "CreateGuidanceResponse",
    "CreateQueryResponse",
    "DeleteAllWebsitesResponse",
    "DeleteCodeRecordResponse",
    "DeleteDocumentRequest",
    "DeleteDocumentResponse",
    "DeleteDocumentsResponse",
    "DeleteGuidanceResponse",
    "DeleteWebsiteResponse",
    "Document",
    "EnableAskAiResponse",
    "Feedback",
    "GetCodeRecordResponse",
    "GetCodeRecordsResponse",
    "GetConversationResolutionResponse",
    "GetConversationResponse",
    "GetDocumentResponse",
    "GetDocumentsResponse",
    "GetFeedbackResponse",
    "GetGuidanceResponse",
    "GetGuidancesResponse",
    "GetHistogramAnalyticsResponse",
    "GetInsightsResponse",
    "GetMcpBmfQueryResponse",
    "GetMcpSemanticQueryResponse",
    "GetQueriesResponse",
    "GetSettingsResponse",
    "GetWebsiteResponse",
    "GetWebsiteStatusResponse",
    "GetWebsitesResponse",
    "GroupBy",
    "Guidance",
    "HistogramAnalyticsBar",
    "HttpValidationError",
    "IndexWebsiteResponse",
    "InsightExample",
    "InsightWithMetadata",
    "JobStatusResponse",
    "LanguageModel",
    "PaginationResponse",
    "PostChatCompletionResponse",
    "Query",
    "QueryStatus",
    "ReconstructIndexResponse",
    "ReindexWebsiteResponse",
    "ReindexingJobRecord",
    "ResolutionFilter",
    "SyncIndexResponse",
    "ToggleAskAiResponse",
    "ToggleStatusResponse",
    "UpdateDocumentResponse",
    "UpdateGuidanceResponse",
    "UpdateReindexingJobStatusResponse",
    "ValidationError",
    "ValidationErrorLocItem",
    "VersionBump",
    "Website",
]
