



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accept_invitation_response import AcceptInvitationResponse
    from .account_deletion_info import AccountDeletionInfo
    from .agent_task import AgentTask
    from .agent_task_list_response import AgentTaskListResponse
    from .agent_task_verification_status import AgentTaskVerificationStatus
    from .approval_call import ApprovalCall
    from .audit_action import AuditAction
    from .audit_event import AuditEvent
    from .audit_event_action_category import AuditEventActionCategory
    from .audit_log_list_response import AuditLogListResponse
    from .auth_url_response import AuthUrlResponse
    from .billing_error_response import BillingErrorResponse
    from .business import Business
    from .business_membership_role_ref import BusinessMembershipRoleRef
    from .business_membership_summary import BusinessMembershipSummary
    from .change_password_request import ChangePasswordRequest
    from .channel_demand_count import ChannelDemandCount
    from .channel_demand_summary import ChannelDemandSummary
    from .channel_request_channel import ChannelRequestChannel
    from .chat_history_entry import ChatHistoryEntry
    from .chat_history_entry_role import ChatHistoryEntryRole
    from .chat_request import ChatRequest
    from .chat_request_project_whitelist_mode import ChatRequestProjectWhitelistMode
    from .chat_request_selected_platforms_item import ChatRequestSelectedPlatformsItem
    from .chat_turn_request import ChatTurnRequest
    from .chat_turn_request_selected_platforms_item import ChatTurnRequestSelectedPlatformsItem
    from .chat_view import ChatView
    from .code_error_response import CodeErrorResponse
    from .confirm_password_reset_request import ConfirmPasswordResetRequest
    from .connect_delegated_yandex_request import ConnectDelegatedYandexRequest
    from .connect_telegram_request import ConnectTelegramRequest
    from .connect_vk_request import ConnectVkRequest
    from .connect_yandex_request import ConnectYandexRequest
    from .consent_record import ConsentRecord
    from .consent_required_response import ConsentRequiredResponse
    from .consent_required_response_code import ConsentRequiredResponseCode
    from .content_template import ContentTemplate
    from .content_template_kind import ContentTemplateKind
    from .content_template_request import ContentTemplateRequest
    from .content_template_request_kind import ContentTemplateRequestKind
    from .conversation import Conversation
    from .conversation_title_status import ConversationTitleStatus
    from .create_business_request import CreateBusinessRequest
    from .create_channel_request_request import CreateChannelRequestRequest
    from .create_channel_request_request_channel import CreateChannelRequestRequestChannel
    from .create_content_template_from_source_request import CreateContentTemplateFromSourceRequest
    from .create_conversation_request import CreateConversationRequest
    from .create_invitation_request import CreateInvitationRequest
    from .create_invitation_response import CreateInvitationResponse
    from .create_role_request import CreateRoleRequest
    from .daily_spend_response import DailySpendResponse
    from .delete_account_request import DeleteAccountRequest
    from .description_template_response import DescriptionTemplateResponse
    from .draft_reply_example import DraftReplyExample
    from .draft_reply_request import DraftReplyRequest
    from .draft_reply_response import DraftReplyResponse
    from .drift_alert_settings import DriftAlertSettings
    from .drift_alert_settings_locale import DriftAlertSettingsLocale
    from .email_before_verify_request import EmailBeforeVerifyRequest
    from .error_response import ErrorResponse
    from .google_location_ref import GoogleLocationRef
    from .google_locations_response import GoogleLocationsResponse
    from .google_select_location_request import GoogleSelectLocationRequest
    from .hitl_already_resolved_error import HitlAlreadyResolvedError
    from .hitl_already_resolved_error_error import HitlAlreadyResolvedErrorError
    from .hitl_already_resolved_error_reason import HitlAlreadyResolvedErrorReason
    from .hitl_batch_resolving_error import HitlBatchResolvingError
    from .hitl_batch_resolving_error_error import HitlBatchResolvingErrorError
    from .hitl_batch_resolving_error_reason import HitlBatchResolvingErrorReason
    from .hitl_decision_input import HitlDecisionInput
    from .hitl_decision_input_action import HitlDecisionInputAction
    from .hitl_expired_error import HitlExpiredError
    from .hitl_expired_error_error import HitlExpiredErrorError
    from .hitl_field_not_editable_error import HitlFieldNotEditableError
    from .hitl_non_scalar_field_error import HitlNonScalarFieldError
    from .hitl_reject_reason_too_long_error import HitlRejectReasonTooLongError
    from .hitl_reject_reason_too_long_error_error import HitlRejectReasonTooLongErrorError
    from .hitl_resolve_request import HitlResolveRequest
    from .hitl_resolve_response import HitlResolveResponse
    from .hitl_resolved_call import HitlResolvedCall
    from .hitl_resolved_call_action import HitlResolvedCallAction
    from .hitl_shape_mismatch_error import HitlShapeMismatchError
    from .hitl_shape_mismatch_error_error import HitlShapeMismatchErrorError
    from .integration import Integration
    from .integration_health import IntegrationHealth
    from .integration_health_status import IntegrationHealthStatus
    from .internal_token_response import InternalTokenResponse
    from .invitation_preview import InvitationPreview
    from .invitation_state_error_response import InvitationStateErrorResponse
    from .landing_event_request import LandingEventRequest
    from .landing_event_request_cta import LandingEventRequestCta
    from .list_consents_response import ListConsentsResponse
    from .login_request import LoginRequest
    from .login_response import LoginResponse
    from .me_response import MeResponse
    from .member import Member
    from .member_role import MemberRole
    from .member_user import MemberUser
    from .message import Message
    from .message_attachment import MessageAttachment
    from .message_role import MessageRole
    from .message_tool_call import MessageToolCall
    from .message_tool_result import MessageToolResult
    from .move_conversation_request import MoveConversationRequest
    from .my_permissions_response import MyPermissionsResponse
    from .owner_brief_response import OwnerBriefResponse
    from .password_reset_error_response import PasswordResetErrorResponse
    from .pending_approval import PendingApproval
    from .pending_approval_call import PendingApprovalCall
    from .pending_approval_status import PendingApprovalStatus
    from .pending_deletion_response import PendingDeletionResponse
    from .pending_deletion_response_code import PendingDeletionResponseCode
    from .pending_invitation import PendingInvitation
    from .pending_invitation_created_by import PendingInvitationCreatedBy
    from .permission import Permission
    from .permission_group import PermissionGroup
    from .permission_registry_response import PermissionRegistryResponse
    from .platform import Platform
    from .platform_status import PlatformStatus
    from .post import Post
    from .post_list_response import PostListResponse
    from .post_platform_result import PostPlatformResult
    from .presence_health_response import PresenceHealthResponse
    from .presence_recommendation import PresenceRecommendation
    from .presence_recommendation_area import PresenceRecommendationArea
    from .presence_sub_scores import PresenceSubScores
    from .presence_weights import PresenceWeights
    from .project import Project
    from .project_approval_overrides_value import ProjectApprovalOverridesValue
    from .project_conversation_count_response import ProjectConversationCountResponse
    from .project_delete_response import ProjectDeleteResponse
    from .project_request import ProjectRequest
    from .project_request_approval_overrides_value import ProjectRequestApprovalOverridesValue
    from .project_request_whitelist_mode import ProjectRequestWhitelistMode
    from .project_whitelist_mode import ProjectWhitelistMode
    from .public_channel_vote_request import PublicChannelVoteRequest
    from .public_channel_vote_request_channel import PublicChannelVoteRequestChannel
    from .reconsent_policy import ReconsentPolicy
    from .reconsent_request import ReconsentRequest
    from .refresh_started_response import RefreshStartedResponse
    from .refresh_started_response_status import RefreshStartedResponseStatus
    from .refresh_telegram_request import RefreshTelegramRequest
    from .refresh_telegram_response import RefreshTelegramResponse
    from .refresh_telegram_response_linked_group_status import RefreshTelegramResponseLinkedGroupStatus
    from .refresh_token_response import RefreshTokenResponse
    from .register_consents import RegisterConsents
    from .register_request import RegisterRequest
    from .render_content_template_request import RenderContentTemplateRequest
    from .render_content_template_response import RenderContentTemplateResponse
    from .reply_to_review_request import ReplyToReviewRequest
    from .request_password_reset_request import RequestPasswordResetRequest
    from .requires_reconsent_info import RequiresReconsentInfo
    from .requires_reconsent_info_policies_item import RequiresReconsentInfoPoliciesItem
    from .resume_request import ResumeRequest
    from .resume_request_whitelist_mode import ResumeRequestWhitelistMode
    from .review import Review
    from .review_autopilot_response import ReviewAutopilotResponse
    from .review_delegation_metrics import ReviewDelegationMetrics
    from .review_delegation_week import ReviewDelegationWeek
    from .review_draft_status import ReviewDraftStatus
    from .review_list_response import ReviewListResponse
    from .review_platform_sla import ReviewPlatformSla
    from .review_reply_status import ReviewReplyStatus
    from .review_sla_response import ReviewSlaResponse
    from .review_unanswered_buckets import ReviewUnansweredBuckets
    from .role import Role
    from .search_result import SearchResult
    from .search_result_title_status import SearchResultTitleStatus
    from .sole_owner_business_entry import SoleOwnerBusinessEntry
    from .sole_owner_response import SoleOwnerResponse
    from .sole_owner_response_code import SoleOwnerResponseCode
    from .sse_concurrency_error import SseConcurrencyError
    from .sse_concurrency_error_code import SseConcurrencyErrorCode
    from .sse_event import (
        SseEvent,
        SseEvent_Done,
        SseEvent_Error,
        SseEvent_Text,
        SseEvent_ToolApprovalRequired,
        SseEvent_ToolCall,
        SseEvent_ToolRejected,
        SseEvent_ToolResult,
    )
    from .sse_event_approval_required import SseEventApprovalRequired
    from .sse_event_done import SseEventDone
    from .sse_event_error import SseEventError
    from .sse_event_text import SseEventText
    from .sse_event_tool_call import SseEventToolCall
    from .sse_event_tool_rejected import SseEventToolRejected
    from .sse_event_tool_result import SseEventToolResult
    from .status_ok_response import StatusOkResponse
    from .status_ok_response_status import StatusOkResponseStatus
    from .telegram_connect_error import TelegramConnectError
    from .telegram_login_request import TelegramLoginRequest
    from .telegram_login_request_auth_date import TelegramLoginRequestAuthDate
    from .telegram_login_verified_response import TelegramLoginVerifiedResponse
    from .telegram_owner_link_response import TelegramOwnerLinkResponse
    from .telemetry_event import TelemetryEvent
    from .telemetry_event_event_type import TelemetryEventEventType
    from .titler_conflict_error import TitlerConflictError
    from .titler_conflict_error_error import TitlerConflictErrorError
    from .titler_disabled_error import TitlerDisabledError
    from .titler_disabled_error_error import TitlerDisabledErrorError
    from .tool_approvals_response import ToolApprovalsResponse
    from .tool_entry import ToolEntry
    from .tool_entry_floor import ToolEntryFloor
    from .tool_floor import ToolFloor
    from .tool_names_response import ToolNamesResponse
    from .tool_registry_entry import ToolRegistryEntry
    from .update_business_request import UpdateBusinessRequest
    from .update_conversation_request import UpdateConversationRequest
    from .update_description_template_request import UpdateDescriptionTemplateRequest
    from .update_drift_alert_settings_request import UpdateDriftAlertSettingsRequest
    from .update_drift_alert_settings_request_locale import UpdateDriftAlertSettingsRequestLocale
    from .update_member_role_request import UpdateMemberRoleRequest
    from .update_member_role_response import UpdateMemberRoleResponse
    from .update_owner_brief_request import UpdateOwnerBriefRequest
    from .update_preferred_locale_request import UpdatePreferredLocaleRequest
    from .update_preferred_locale_request_locale import UpdatePreferredLocaleRequestLocale
    from .update_profile_request import UpdateProfileRequest
    from .update_review_autopilot_request import UpdateReviewAutopilotRequest
    from .update_role_request import UpdateRoleRequest
    from .update_schedule_request import UpdateScheduleRequest
    from .update_tool_approvals_request import UpdateToolApprovalsRequest
    from .update_voice_profile_request import UpdateVoiceProfileRequest
    from .update_voice_tone_request import UpdateVoiceToneRequest
    from .upload_logo_request import UploadLogoRequest
    from .usage_log import UsageLog
    from .user import User
    from .user_preferred_locale import UserPreferredLocale
    from .validation_error_response import ValidationErrorResponse
    from .verify_confirm_request import VerifyConfirmRequest
    from .verify_integrations_response import VerifyIntegrationsResponse
    from .verify_yandex_access_request import VerifyYandexAccessRequest
    from .verify_yandex_access_response import VerifyYandexAccessResponse
    from .version_mismatch_response import VersionMismatchResponse
    from .version_mismatch_response_code import VersionMismatchResponseCode
    from .vk_community import VkCommunity
    from .voice_profile_response import VoiceProfileResponse
    from .waitlist_request import WaitlistRequest
    from .waitlist_request_pain import WaitlistRequestPain
    from .waitlist_request_plan import WaitlistRequestPlan
    from .waitlist_request_source import WaitlistRequestSource
    from .waitlist_request_sphere import WaitlistRequestSphere
    from .weekly_value_recap import WeeklyValueRecap
    from .yandex_companies_response import YandexCompaniesResponse
    from .yandex_company_entry import YandexCompanyEntry
    from .yandex_cookies_request import YandexCookiesRequest
    from .yandex_delegated_config_response import YandexDelegatedConfigResponse
    from .yandex_probe_response import YandexProbeResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AcceptInvitationResponse": ".accept_invitation_response",
    "AccountDeletionInfo": ".account_deletion_info",
    "AgentTask": ".agent_task",
    "AgentTaskListResponse": ".agent_task_list_response",
    "AgentTaskVerificationStatus": ".agent_task_verification_status",
    "ApprovalCall": ".approval_call",
    "AuditAction": ".audit_action",
    "AuditEvent": ".audit_event",
    "AuditEventActionCategory": ".audit_event_action_category",
    "AuditLogListResponse": ".audit_log_list_response",
    "AuthUrlResponse": ".auth_url_response",
    "BillingErrorResponse": ".billing_error_response",
    "Business": ".business",
    "BusinessMembershipRoleRef": ".business_membership_role_ref",
    "BusinessMembershipSummary": ".business_membership_summary",
    "ChangePasswordRequest": ".change_password_request",
    "ChannelDemandCount": ".channel_demand_count",
    "ChannelDemandSummary": ".channel_demand_summary",
    "ChannelRequestChannel": ".channel_request_channel",
    "ChatHistoryEntry": ".chat_history_entry",
    "ChatHistoryEntryRole": ".chat_history_entry_role",
    "ChatRequest": ".chat_request",
    "ChatRequestProjectWhitelistMode": ".chat_request_project_whitelist_mode",
    "ChatRequestSelectedPlatformsItem": ".chat_request_selected_platforms_item",
    "ChatTurnRequest": ".chat_turn_request",
    "ChatTurnRequestSelectedPlatformsItem": ".chat_turn_request_selected_platforms_item",
    "ChatView": ".chat_view",
    "CodeErrorResponse": ".code_error_response",
    "ConfirmPasswordResetRequest": ".confirm_password_reset_request",
    "ConnectDelegatedYandexRequest": ".connect_delegated_yandex_request",
    "ConnectTelegramRequest": ".connect_telegram_request",
    "ConnectVkRequest": ".connect_vk_request",
    "ConnectYandexRequest": ".connect_yandex_request",
    "ConsentRecord": ".consent_record",
    "ConsentRequiredResponse": ".consent_required_response",
    "ConsentRequiredResponseCode": ".consent_required_response_code",
    "ContentTemplate": ".content_template",
    "ContentTemplateKind": ".content_template_kind",
    "ContentTemplateRequest": ".content_template_request",
    "ContentTemplateRequestKind": ".content_template_request_kind",
    "Conversation": ".conversation",
    "ConversationTitleStatus": ".conversation_title_status",
    "CreateBusinessRequest": ".create_business_request",
    "CreateChannelRequestRequest": ".create_channel_request_request",
    "CreateChannelRequestRequestChannel": ".create_channel_request_request_channel",
    "CreateContentTemplateFromSourceRequest": ".create_content_template_from_source_request",
    "CreateConversationRequest": ".create_conversation_request",
    "CreateInvitationRequest": ".create_invitation_request",
    "CreateInvitationResponse": ".create_invitation_response",
    "CreateRoleRequest": ".create_role_request",
    "DailySpendResponse": ".daily_spend_response",
    "DeleteAccountRequest": ".delete_account_request",
    "DescriptionTemplateResponse": ".description_template_response",
    "DraftReplyExample": ".draft_reply_example",
    "DraftReplyRequest": ".draft_reply_request",
    "DraftReplyResponse": ".draft_reply_response",
    "DriftAlertSettings": ".drift_alert_settings",
    "DriftAlertSettingsLocale": ".drift_alert_settings_locale",
    "EmailBeforeVerifyRequest": ".email_before_verify_request",
    "ErrorResponse": ".error_response",
    "GoogleLocationRef": ".google_location_ref",
    "GoogleLocationsResponse": ".google_locations_response",
    "GoogleSelectLocationRequest": ".google_select_location_request",
    "HitlAlreadyResolvedError": ".hitl_already_resolved_error",
    "HitlAlreadyResolvedErrorError": ".hitl_already_resolved_error_error",
    "HitlAlreadyResolvedErrorReason": ".hitl_already_resolved_error_reason",
    "HitlBatchResolvingError": ".hitl_batch_resolving_error",
    "HitlBatchResolvingErrorError": ".hitl_batch_resolving_error_error",
    "HitlBatchResolvingErrorReason": ".hitl_batch_resolving_error_reason",
    "HitlDecisionInput": ".hitl_decision_input",
    "HitlDecisionInputAction": ".hitl_decision_input_action",
    "HitlExpiredError": ".hitl_expired_error",
    "HitlExpiredErrorError": ".hitl_expired_error_error",
    "HitlFieldNotEditableError": ".hitl_field_not_editable_error",
    "HitlNonScalarFieldError": ".hitl_non_scalar_field_error",
    "HitlRejectReasonTooLongError": ".hitl_reject_reason_too_long_error",
    "HitlRejectReasonTooLongErrorError": ".hitl_reject_reason_too_long_error_error",
    "HitlResolveRequest": ".hitl_resolve_request",
    "HitlResolveResponse": ".hitl_resolve_response",
    "HitlResolvedCall": ".hitl_resolved_call",
    "HitlResolvedCallAction": ".hitl_resolved_call_action",
    "HitlShapeMismatchError": ".hitl_shape_mismatch_error",
    "HitlShapeMismatchErrorError": ".hitl_shape_mismatch_error_error",
    "Integration": ".integration",
    "IntegrationHealth": ".integration_health",
    "IntegrationHealthStatus": ".integration_health_status",
    "InternalTokenResponse": ".internal_token_response",
    "InvitationPreview": ".invitation_preview",
    "InvitationStateErrorResponse": ".invitation_state_error_response",
    "LandingEventRequest": ".landing_event_request",
    "LandingEventRequestCta": ".landing_event_request_cta",
    "ListConsentsResponse": ".list_consents_response",
    "LoginRequest": ".login_request",
    "LoginResponse": ".login_response",
    "MeResponse": ".me_response",
    "Member": ".member",
    "MemberRole": ".member_role",
    "MemberUser": ".member_user",
    "Message": ".message",
    "MessageAttachment": ".message_attachment",
    "MessageRole": ".message_role",
    "MessageToolCall": ".message_tool_call",
    "MessageToolResult": ".message_tool_result",
    "MoveConversationRequest": ".move_conversation_request",
    "MyPermissionsResponse": ".my_permissions_response",
    "OwnerBriefResponse": ".owner_brief_response",
    "PasswordResetErrorResponse": ".password_reset_error_response",
    "PendingApproval": ".pending_approval",
    "PendingApprovalCall": ".pending_approval_call",
    "PendingApprovalStatus": ".pending_approval_status",
    "PendingDeletionResponse": ".pending_deletion_response",
    "PendingDeletionResponseCode": ".pending_deletion_response_code",
    "PendingInvitation": ".pending_invitation",
    "PendingInvitationCreatedBy": ".pending_invitation_created_by",
    "Permission": ".permission",
    "PermissionGroup": ".permission_group",
    "PermissionRegistryResponse": ".permission_registry_response",
    "Platform": ".platform",
    "PlatformStatus": ".platform_status",
    "Post": ".post",
    "PostListResponse": ".post_list_response",
    "PostPlatformResult": ".post_platform_result",
    "PresenceHealthResponse": ".presence_health_response",
    "PresenceRecommendation": ".presence_recommendation",
    "PresenceRecommendationArea": ".presence_recommendation_area",
    "PresenceSubScores": ".presence_sub_scores",
    "PresenceWeights": ".presence_weights",
    "Project": ".project",
    "ProjectApprovalOverridesValue": ".project_approval_overrides_value",
    "ProjectConversationCountResponse": ".project_conversation_count_response",
    "ProjectDeleteResponse": ".project_delete_response",
    "ProjectRequest": ".project_request",
    "ProjectRequestApprovalOverridesValue": ".project_request_approval_overrides_value",
    "ProjectRequestWhitelistMode": ".project_request_whitelist_mode",
    "ProjectWhitelistMode": ".project_whitelist_mode",
    "PublicChannelVoteRequest": ".public_channel_vote_request",
    "PublicChannelVoteRequestChannel": ".public_channel_vote_request_channel",
    "ReconsentPolicy": ".reconsent_policy",
    "ReconsentRequest": ".reconsent_request",
    "RefreshStartedResponse": ".refresh_started_response",
    "RefreshStartedResponseStatus": ".refresh_started_response_status",
    "RefreshTelegramRequest": ".refresh_telegram_request",
    "RefreshTelegramResponse": ".refresh_telegram_response",
    "RefreshTelegramResponseLinkedGroupStatus": ".refresh_telegram_response_linked_group_status",
    "RefreshTokenResponse": ".refresh_token_response",
    "RegisterConsents": ".register_consents",
    "RegisterRequest": ".register_request",
    "RenderContentTemplateRequest": ".render_content_template_request",
    "RenderContentTemplateResponse": ".render_content_template_response",
    "ReplyToReviewRequest": ".reply_to_review_request",
    "RequestPasswordResetRequest": ".request_password_reset_request",
    "RequiresReconsentInfo": ".requires_reconsent_info",
    "RequiresReconsentInfoPoliciesItem": ".requires_reconsent_info_policies_item",
    "ResumeRequest": ".resume_request",
    "ResumeRequestWhitelistMode": ".resume_request_whitelist_mode",
    "Review": ".review",
    "ReviewAutopilotResponse": ".review_autopilot_response",
    "ReviewDelegationMetrics": ".review_delegation_metrics",
    "ReviewDelegationWeek": ".review_delegation_week",
    "ReviewDraftStatus": ".review_draft_status",
    "ReviewListResponse": ".review_list_response",
    "ReviewPlatformSla": ".review_platform_sla",
    "ReviewReplyStatus": ".review_reply_status",
    "ReviewSlaResponse": ".review_sla_response",
    "ReviewUnansweredBuckets": ".review_unanswered_buckets",
    "Role": ".role",
    "SearchResult": ".search_result",
    "SearchResultTitleStatus": ".search_result_title_status",
    "SoleOwnerBusinessEntry": ".sole_owner_business_entry",
    "SoleOwnerResponse": ".sole_owner_response",
    "SoleOwnerResponseCode": ".sole_owner_response_code",
    "SseConcurrencyError": ".sse_concurrency_error",
    "SseConcurrencyErrorCode": ".sse_concurrency_error_code",
    "SseEvent": ".sse_event",
    "SseEventApprovalRequired": ".sse_event_approval_required",
    "SseEventDone": ".sse_event_done",
    "SseEventError": ".sse_event_error",
    "SseEventText": ".sse_event_text",
    "SseEventToolCall": ".sse_event_tool_call",
    "SseEventToolRejected": ".sse_event_tool_rejected",
    "SseEventToolResult": ".sse_event_tool_result",
    "SseEvent_Done": ".sse_event",
    "SseEvent_Error": ".sse_event",
    "SseEvent_Text": ".sse_event",
    "SseEvent_ToolApprovalRequired": ".sse_event",
    "SseEvent_ToolCall": ".sse_event",
    "SseEvent_ToolRejected": ".sse_event",
    "SseEvent_ToolResult": ".sse_event",
    "StatusOkResponse": ".status_ok_response",
    "StatusOkResponseStatus": ".status_ok_response_status",
    "TelegramConnectError": ".telegram_connect_error",
    "TelegramLoginRequest": ".telegram_login_request",
    "TelegramLoginRequestAuthDate": ".telegram_login_request_auth_date",
    "TelegramLoginVerifiedResponse": ".telegram_login_verified_response",
    "TelegramOwnerLinkResponse": ".telegram_owner_link_response",
    "TelemetryEvent": ".telemetry_event",
    "TelemetryEventEventType": ".telemetry_event_event_type",
    "TitlerConflictError": ".titler_conflict_error",
    "TitlerConflictErrorError": ".titler_conflict_error_error",
    "TitlerDisabledError": ".titler_disabled_error",
    "TitlerDisabledErrorError": ".titler_disabled_error_error",
    "ToolApprovalsResponse": ".tool_approvals_response",
    "ToolEntry": ".tool_entry",
    "ToolEntryFloor": ".tool_entry_floor",
    "ToolFloor": ".tool_floor",
    "ToolNamesResponse": ".tool_names_response",
    "ToolRegistryEntry": ".tool_registry_entry",
    "UpdateBusinessRequest": ".update_business_request",
    "UpdateConversationRequest": ".update_conversation_request",
    "UpdateDescriptionTemplateRequest": ".update_description_template_request",
    "UpdateDriftAlertSettingsRequest": ".update_drift_alert_settings_request",
    "UpdateDriftAlertSettingsRequestLocale": ".update_drift_alert_settings_request_locale",
    "UpdateMemberRoleRequest": ".update_member_role_request",
    "UpdateMemberRoleResponse": ".update_member_role_response",
    "UpdateOwnerBriefRequest": ".update_owner_brief_request",
    "UpdatePreferredLocaleRequest": ".update_preferred_locale_request",
    "UpdatePreferredLocaleRequestLocale": ".update_preferred_locale_request_locale",
    "UpdateProfileRequest": ".update_profile_request",
    "UpdateReviewAutopilotRequest": ".update_review_autopilot_request",
    "UpdateRoleRequest": ".update_role_request",
    "UpdateScheduleRequest": ".update_schedule_request",
    "UpdateToolApprovalsRequest": ".update_tool_approvals_request",
    "UpdateVoiceProfileRequest": ".update_voice_profile_request",
    "UpdateVoiceToneRequest": ".update_voice_tone_request",
    "UploadLogoRequest": ".upload_logo_request",
    "UsageLog": ".usage_log",
    "User": ".user",
    "UserPreferredLocale": ".user_preferred_locale",
    "ValidationErrorResponse": ".validation_error_response",
    "VerifyConfirmRequest": ".verify_confirm_request",
    "VerifyIntegrationsResponse": ".verify_integrations_response",
    "VerifyYandexAccessRequest": ".verify_yandex_access_request",
    "VerifyYandexAccessResponse": ".verify_yandex_access_response",
    "VersionMismatchResponse": ".version_mismatch_response",
    "VersionMismatchResponseCode": ".version_mismatch_response_code",
    "VkCommunity": ".vk_community",
    "VoiceProfileResponse": ".voice_profile_response",
    "WaitlistRequest": ".waitlist_request",
    "WaitlistRequestPain": ".waitlist_request_pain",
    "WaitlistRequestPlan": ".waitlist_request_plan",
    "WaitlistRequestSource": ".waitlist_request_source",
    "WaitlistRequestSphere": ".waitlist_request_sphere",
    "WeeklyValueRecap": ".weekly_value_recap",
    "YandexCompaniesResponse": ".yandex_companies_response",
    "YandexCompanyEntry": ".yandex_company_entry",
    "YandexCookiesRequest": ".yandex_cookies_request",
    "YandexDelegatedConfigResponse": ".yandex_delegated_config_response",
    "YandexProbeResponse": ".yandex_probe_response",
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
    "AcceptInvitationResponse",
    "AccountDeletionInfo",
    "AgentTask",
    "AgentTaskListResponse",
    "AgentTaskVerificationStatus",
    "ApprovalCall",
    "AuditAction",
    "AuditEvent",
    "AuditEventActionCategory",
    "AuditLogListResponse",
    "AuthUrlResponse",
    "BillingErrorResponse",
    "Business",
    "BusinessMembershipRoleRef",
    "BusinessMembershipSummary",
    "ChangePasswordRequest",
    "ChannelDemandCount",
    "ChannelDemandSummary",
    "ChannelRequestChannel",
    "ChatHistoryEntry",
    "ChatHistoryEntryRole",
    "ChatRequest",
    "ChatRequestProjectWhitelistMode",
    "ChatRequestSelectedPlatformsItem",
    "ChatTurnRequest",
    "ChatTurnRequestSelectedPlatformsItem",
    "ChatView",
    "CodeErrorResponse",
    "ConfirmPasswordResetRequest",
    "ConnectDelegatedYandexRequest",
    "ConnectTelegramRequest",
    "ConnectVkRequest",
    "ConnectYandexRequest",
    "ConsentRecord",
    "ConsentRequiredResponse",
    "ConsentRequiredResponseCode",
    "ContentTemplate",
    "ContentTemplateKind",
    "ContentTemplateRequest",
    "ContentTemplateRequestKind",
    "Conversation",
    "ConversationTitleStatus",
    "CreateBusinessRequest",
    "CreateChannelRequestRequest",
    "CreateChannelRequestRequestChannel",
    "CreateContentTemplateFromSourceRequest",
    "CreateConversationRequest",
    "CreateInvitationRequest",
    "CreateInvitationResponse",
    "CreateRoleRequest",
    "DailySpendResponse",
    "DeleteAccountRequest",
    "DescriptionTemplateResponse",
    "DraftReplyExample",
    "DraftReplyRequest",
    "DraftReplyResponse",
    "DriftAlertSettings",
    "DriftAlertSettingsLocale",
    "EmailBeforeVerifyRequest",
    "ErrorResponse",
    "GoogleLocationRef",
    "GoogleLocationsResponse",
    "GoogleSelectLocationRequest",
    "HitlAlreadyResolvedError",
    "HitlAlreadyResolvedErrorError",
    "HitlAlreadyResolvedErrorReason",
    "HitlBatchResolvingError",
    "HitlBatchResolvingErrorError",
    "HitlBatchResolvingErrorReason",
    "HitlDecisionInput",
    "HitlDecisionInputAction",
    "HitlExpiredError",
    "HitlExpiredErrorError",
    "HitlFieldNotEditableError",
    "HitlNonScalarFieldError",
    "HitlRejectReasonTooLongError",
    "HitlRejectReasonTooLongErrorError",
    "HitlResolveRequest",
    "HitlResolveResponse",
    "HitlResolvedCall",
    "HitlResolvedCallAction",
    "HitlShapeMismatchError",
    "HitlShapeMismatchErrorError",
    "Integration",
    "IntegrationHealth",
    "IntegrationHealthStatus",
    "InternalTokenResponse",
    "InvitationPreview",
    "InvitationStateErrorResponse",
    "LandingEventRequest",
    "LandingEventRequestCta",
    "ListConsentsResponse",
    "LoginRequest",
    "LoginResponse",
    "MeResponse",
    "Member",
    "MemberRole",
    "MemberUser",
    "Message",
    "MessageAttachment",
    "MessageRole",
    "MessageToolCall",
    "MessageToolResult",
    "MoveConversationRequest",
    "MyPermissionsResponse",
    "OwnerBriefResponse",
    "PasswordResetErrorResponse",
    "PendingApproval",
    "PendingApprovalCall",
    "PendingApprovalStatus",
    "PendingDeletionResponse",
    "PendingDeletionResponseCode",
    "PendingInvitation",
    "PendingInvitationCreatedBy",
    "Permission",
    "PermissionGroup",
    "PermissionRegistryResponse",
    "Platform",
    "PlatformStatus",
    "Post",
    "PostListResponse",
    "PostPlatformResult",
    "PresenceHealthResponse",
    "PresenceRecommendation",
    "PresenceRecommendationArea",
    "PresenceSubScores",
    "PresenceWeights",
    "Project",
    "ProjectApprovalOverridesValue",
    "ProjectConversationCountResponse",
    "ProjectDeleteResponse",
    "ProjectRequest",
    "ProjectRequestApprovalOverridesValue",
    "ProjectRequestWhitelistMode",
    "ProjectWhitelistMode",
    "PublicChannelVoteRequest",
    "PublicChannelVoteRequestChannel",
    "ReconsentPolicy",
    "ReconsentRequest",
    "RefreshStartedResponse",
    "RefreshStartedResponseStatus",
    "RefreshTelegramRequest",
    "RefreshTelegramResponse",
    "RefreshTelegramResponseLinkedGroupStatus",
    "RefreshTokenResponse",
    "RegisterConsents",
    "RegisterRequest",
    "RenderContentTemplateRequest",
    "RenderContentTemplateResponse",
    "ReplyToReviewRequest",
    "RequestPasswordResetRequest",
    "RequiresReconsentInfo",
    "RequiresReconsentInfoPoliciesItem",
    "ResumeRequest",
    "ResumeRequestWhitelistMode",
    "Review",
    "ReviewAutopilotResponse",
    "ReviewDelegationMetrics",
    "ReviewDelegationWeek",
    "ReviewDraftStatus",
    "ReviewListResponse",
    "ReviewPlatformSla",
    "ReviewReplyStatus",
    "ReviewSlaResponse",
    "ReviewUnansweredBuckets",
    "Role",
    "SearchResult",
    "SearchResultTitleStatus",
    "SoleOwnerBusinessEntry",
    "SoleOwnerResponse",
    "SoleOwnerResponseCode",
    "SseConcurrencyError",
    "SseConcurrencyErrorCode",
    "SseEvent",
    "SseEventApprovalRequired",
    "SseEventDone",
    "SseEventError",
    "SseEventText",
    "SseEventToolCall",
    "SseEventToolRejected",
    "SseEventToolResult",
    "SseEvent_Done",
    "SseEvent_Error",
    "SseEvent_Text",
    "SseEvent_ToolApprovalRequired",
    "SseEvent_ToolCall",
    "SseEvent_ToolRejected",
    "SseEvent_ToolResult",
    "StatusOkResponse",
    "StatusOkResponseStatus",
    "TelegramConnectError",
    "TelegramLoginRequest",
    "TelegramLoginRequestAuthDate",
    "TelegramLoginVerifiedResponse",
    "TelegramOwnerLinkResponse",
    "TelemetryEvent",
    "TelemetryEventEventType",
    "TitlerConflictError",
    "TitlerConflictErrorError",
    "TitlerDisabledError",
    "TitlerDisabledErrorError",
    "ToolApprovalsResponse",
    "ToolEntry",
    "ToolEntryFloor",
    "ToolFloor",
    "ToolNamesResponse",
    "ToolRegistryEntry",
    "UpdateBusinessRequest",
    "UpdateConversationRequest",
    "UpdateDescriptionTemplateRequest",
    "UpdateDriftAlertSettingsRequest",
    "UpdateDriftAlertSettingsRequestLocale",
    "UpdateMemberRoleRequest",
    "UpdateMemberRoleResponse",
    "UpdateOwnerBriefRequest",
    "UpdatePreferredLocaleRequest",
    "UpdatePreferredLocaleRequestLocale",
    "UpdateProfileRequest",
    "UpdateReviewAutopilotRequest",
    "UpdateRoleRequest",
    "UpdateScheduleRequest",
    "UpdateToolApprovalsRequest",
    "UpdateVoiceProfileRequest",
    "UpdateVoiceToneRequest",
    "UploadLogoRequest",
    "UsageLog",
    "User",
    "UserPreferredLocale",
    "ValidationErrorResponse",
    "VerifyConfirmRequest",
    "VerifyIntegrationsResponse",
    "VerifyYandexAccessRequest",
    "VerifyYandexAccessResponse",
    "VersionMismatchResponse",
    "VersionMismatchResponseCode",
    "VkCommunity",
    "VoiceProfileResponse",
    "WaitlistRequest",
    "WaitlistRequestPain",
    "WaitlistRequestPlan",
    "WaitlistRequestSource",
    "WaitlistRequestSphere",
    "WeeklyValueRecap",
    "YandexCompaniesResponse",
    "YandexCompanyEntry",
    "YandexCookiesRequest",
    "YandexDelegatedConfigResponse",
    "YandexProbeResponse",
]
