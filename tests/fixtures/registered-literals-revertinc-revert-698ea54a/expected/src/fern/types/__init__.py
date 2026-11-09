



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accounting_create_or_update_account_request import AccountingCreateOrUpdateAccountRequest
    from .accounting_create_or_update_account_response import AccountingCreateOrUpdateAccountResponse
    from .accounting_create_or_update_expense_request import AccountingCreateOrUpdateExpenseRequest
    from .accounting_create_or_update_expense_response import AccountingCreateOrUpdateExpenseResponse
    from .accounting_create_or_update_vendor_request import AccountingCreateOrUpdateVendorRequest
    from .accounting_create_or_update_vendor_response import AccountingCreateOrUpdateVendorResponse
    from .accounting_delete_account_response import AccountingDeleteAccountResponse
    from .accounting_delete_expense_response import AccountingDeleteExpenseResponse
    from .accounting_delete_vendor_response import AccountingDeleteVendorResponse
    from .accounting_get_account_response import AccountingGetAccountResponse
    from .accounting_get_accounts_response import AccountingGetAccountsResponse
    from .accounting_get_expense_response import AccountingGetExpenseResponse
    from .accounting_get_expenses_response import AccountingGetExpensesResponse
    from .accounting_get_vendor_response import AccountingGetVendorResponse
    from .accounting_get_vendors_response import AccountingGetVendorsResponse
    from .accounting_proxy_response import AccountingProxyResponse
    from .ats_create_or_update_candidate_request import AtsCreateOrUpdateCandidateRequest
    from .ats_create_or_update_candidate_response import AtsCreateOrUpdateCandidateResponse
    from .ats_create_or_update_department_request import AtsCreateOrUpdateDepartmentRequest
    from .ats_create_or_update_department_response import AtsCreateOrUpdateDepartmentResponse
    from .ats_create_or_update_job_request import AtsCreateOrUpdateJobRequest
    from .ats_create_or_update_job_response import AtsCreateOrUpdateJobResponse
    from .ats_create_or_update_offer_request import AtsCreateOrUpdateOfferRequest
    from .ats_create_or_update_offer_response import AtsCreateOrUpdateOfferResponse
    from .ats_delete_candidate_response import AtsDeleteCandidateResponse
    from .ats_delete_department_response import AtsDeleteDepartmentResponse
    from .ats_delete_job_response import AtsDeleteJobResponse
    from .ats_delete_offer_response import AtsDeleteOfferResponse
    from .ats_get_candidate_response import AtsGetCandidateResponse
    from .ats_get_candidates_response import AtsGetCandidatesResponse
    from .ats_get_department_response import AtsGetDepartmentResponse
    from .ats_get_departments_response import AtsGetDepartmentsResponse
    from .ats_get_job_response import AtsGetJobResponse
    from .ats_get_jobs_response import AtsGetJobsResponse
    from .ats_get_offer_response import AtsGetOfferResponse
    from .ats_get_offers_response import AtsGetOffersResponse
    from .ats_proxy_response import AtsProxyResponse
    from .chat_createor_update_message_request import ChatCreateorUpdateMessageRequest
    from .chat_createor_update_message_response import ChatCreateorUpdateMessageResponse
    from .chat_get_channels_response import ChatGetChannelsResponse
    from .chat_get_users_response import ChatGetUsersResponse
    from .common_account import CommonAccount
    from .common_analytics import CommonAnalytics
    from .common_app import CommonApp
    from .common_app_config import CommonAppConfig
    from .common_base_error import CommonBaseError
    from .common_channel import CommonChannel
    from .common_comment_ticket import CommonCommentTicket
    from .common_comment_ticket_write import CommonCommentTicketWrite
    from .common_common_unified_fields import CommonCommonUnifiedFields
    from .common_company import CommonCompany
    from .common_company_address import CommonCompanyAddress
    from .common_company_association import CommonCompanyAssociation
    from .common_connected_apps import CommonConnectedApps
    from .common_connection import CommonConnection
    from .common_contact import CommonContact
    from .common_contact_association import CommonContactAssociation
    from .common_contact_read import CommonContactRead
    from .common_contact_write import CommonContactWrite
    from .common_deal import CommonDeal
    from .common_deal_association import CommonDealAssociation
    from .common_deal_read import CommonDealRead
    from .common_deal_write import CommonDealWrite
    from .common_environment import CommonEnvironment
    from .common_event import CommonEvent
    from .common_event_association import CommonEventAssociation
    from .common_event_read import CommonEventRead
    from .common_event_write import CommonEventWrite
    from .common_lead import CommonLead
    from .common_lead_association import CommonLeadAssociation
    from .common_lead_read import CommonLeadRead
    from .common_lead_write import CommonLeadWrite
    from .common_message import CommonMessage
    from .common_note import CommonNote
    from .common_note_association import CommonNoteAssociation
    from .common_note_read import CommonNoteRead
    from .common_note_write import CommonNoteWrite
    from .common_recent_api_calls import CommonRecentApiCalls
    from .common_recent_connections import CommonRecentConnections
    from .common_response_status import CommonResponseStatus
    from .common_revert_user import CommonRevertUser
    from .common_standard_object import CommonStandardObject
    from .common_summary_api_calls import CommonSummaryApiCalls
    from .common_svix_account import CommonSvixAccount
    from .common_task import CommonTask
    from .common_task_association import CommonTaskAssociation
    from .common_task_read import CommonTaskRead
    from .common_task_ticket import CommonTaskTicket
    from .common_task_ticket_write import CommonTaskTicketWrite
    from .common_task_write import CommonTaskWrite
    from .common_ticket_priority import CommonTicketPriority
    from .common_ticket_status import CommonTicketStatus
    from .common_tpid import CommonTpid
    from .common_user import CommonUser
    from .common_user_association import CommonUserAssociation
    from .common_user_chat import CommonUserChat
    from .common_user_write import CommonUserWrite
    from .connection_import import ConnectionImport
    from .connection_status import ConnectionStatus
    from .create_account_field_mapping_response import CreateAccountFieldMappingResponse
    from .create_connection_webhook_response import CreateConnectionWebhookResponse
    from .create_field_mapping_response import CreateFieldMappingResponse
    from .crm_create_or_update_company_response import CrmCreateOrUpdateCompanyResponse
    from .crm_create_or_update_contact_request import CrmCreateOrUpdateContactRequest
    from .crm_create_or_update_contact_response import CrmCreateOrUpdateContactResponse
    from .crm_create_or_update_deal_request import CrmCreateOrUpdateDealRequest
    from .crm_create_or_update_deal_response import CrmCreateOrUpdateDealResponse
    from .crm_create_or_update_event_request import CrmCreateOrUpdateEventRequest
    from .crm_create_or_update_event_response import CrmCreateOrUpdateEventResponse
    from .crm_create_or_update_lead_request import CrmCreateOrUpdateLeadRequest
    from .crm_create_or_update_lead_response import CrmCreateOrUpdateLeadResponse
    from .crm_create_or_update_note_request import CrmCreateOrUpdateNoteRequest
    from .crm_create_or_update_note_response import CrmCreateOrUpdateNoteResponse
    from .crm_create_or_update_task_request import CrmCreateOrUpdateTaskRequest
    from .crm_create_or_update_task_response import CrmCreateOrUpdateTaskResponse
    from .crm_create_or_update_user_response import CrmCreateOrUpdateUserResponse
    from .crm_delete_event_response import CrmDeleteEventResponse
    from .crm_field_details_type import CrmFieldDetailsType
    from .crm_field_details_type_read import CrmFieldDetailsTypeRead
    from .crm_field_details_type_request import CrmFieldDetailsTypeRequest
    from .crm_get_companies_response import CrmGetCompaniesResponse
    from .crm_get_company_response import CrmGetCompanyResponse
    from .crm_get_contact_response import CrmGetContactResponse
    from .crm_get_contacts_response import CrmGetContactsResponse
    from .crm_get_deal_response import CrmGetDealResponse
    from .crm_get_deals_response import CrmGetDealsResponse
    from .crm_get_event_response import CrmGetEventResponse
    from .crm_get_events_response import CrmGetEventsResponse
    from .crm_get_lead_response import CrmGetLeadResponse
    from .crm_get_leads_response import CrmGetLeadsResponse
    from .crm_get_note_response import CrmGetNoteResponse
    from .crm_get_notes_response import CrmGetNotesResponse
    from .crm_get_object_properties_response import CrmGetObjectPropertiesResponse
    from .crm_get_task_response import CrmGetTaskResponse
    from .crm_get_tasks_response import CrmGetTasksResponse
    from .crm_get_user_response import CrmGetUserResponse
    from .crm_get_users_response import CrmGetUsersResponse
    from .crm_metadata import CrmMetadata
    from .crm_metadata_response import CrmMetadataResponse
    from .crm_proxy_response import CrmProxyResponse
    from .crm_search_companies_response import CrmSearchCompaniesResponse
    from .crm_search_contacts_response import CrmSearchContactsResponse
    from .crm_search_deals_response import CrmSearchDealsResponse
    from .crm_search_events_response import CrmSearchEventsResponse
    from .crm_search_leads_response import CrmSearchLeadsResponse
    from .crm_search_notes_response import CrmSearchNotesResponse
    from .crm_search_tasks_response import CrmSearchTasksResponse
    from .crm_search_users_response import CrmSearchUsersResponse
    from .crm_set_object_properties_request import CrmSetObjectPropertiesRequest
    from .crm_set_object_properties_response import CrmSetObjectPropertiesResponse
    from .crm_status import CrmStatus
    from .delete_account_field_mapping_config_response import DeleteAccountFieldMappingConfigResponse
    from .delete_connection_response import DeleteConnectionResponse
    from .delete_connection_webhook_response import DeleteConnectionWebhookResponse
    from .delete_field_mapping_response import DeleteFieldMappingResponse
    from .field_mapping_type import FieldMappingType
    from .get_all_connection_response import GetAllConnectionResponse
    from .get_connect_status_response import GetConnectStatusResponse
    from .get_connection_response import GetConnectionResponse
    from .get_connection_webhook_response import GetConnectionWebhookResponse
    from .get_field_mapping_config_response import GetFieldMappingConfigResponse
    from .get_field_mappings_response import GetFieldMappingsResponse
    from .import_connections_response import ImportConnectionsResponse
    from .internal_create_telemetry_entry_response import InternalCreateTelemetryEntryResponse
    from .internal_delete_revert_app_response import InternalDeleteRevertAppResponse
    from .internal_get_account_details_response import InternalGetAccountDetailsResponse
    from .internal_get_analytics_response import InternalGetAnalyticsResponse
    from .internal_recent_api_calls import InternalRecentApiCalls
    from .internal_recent_app_api_calls_response import InternalRecentAppApiCallsResponse
    from .internal_svix_account_response import InternalSvixAccountResponse
    from .internal_svix_magic_link_response import InternalSvixMagicLinkResponse
    from .internalset_onboarding_response import InternalsetOnboardingResponse
    from .mappable_field_type import MappableFieldType
    from .ticket_create_or_update_comment_request import TicketCreateOrUpdateCommentRequest
    from .ticket_create_or_update_comment_response import TicketCreateOrUpdateCommentResponse
    from .ticket_create_or_update_task_request import TicketCreateOrUpdateTaskRequest
    from .ticket_create_or_update_task_response import TicketCreateOrUpdateTaskResponse
    from .ticket_get_collections_response import TicketGetCollectionsResponse
    from .ticket_get_comment_response import TicketGetCommentResponse
    from .ticket_get_comments_response import TicketGetCommentsResponse
    from .ticket_get_task_response import TicketGetTaskResponse
    from .ticket_get_tasks_response import TicketGetTasksResponse
    from .ticket_get_user_response import TicketGetUserResponse
    from .ticket_get_users_response import TicketGetUsersResponse
    from .ticket_proxy_response import TicketProxyResponse
    from .trigger_sync_response import TriggerSyncResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AccountingCreateOrUpdateAccountRequest": ".accounting_create_or_update_account_request",
    "AccountingCreateOrUpdateAccountResponse": ".accounting_create_or_update_account_response",
    "AccountingCreateOrUpdateExpenseRequest": ".accounting_create_or_update_expense_request",
    "AccountingCreateOrUpdateExpenseResponse": ".accounting_create_or_update_expense_response",
    "AccountingCreateOrUpdateVendorRequest": ".accounting_create_or_update_vendor_request",
    "AccountingCreateOrUpdateVendorResponse": ".accounting_create_or_update_vendor_response",
    "AccountingDeleteAccountResponse": ".accounting_delete_account_response",
    "AccountingDeleteExpenseResponse": ".accounting_delete_expense_response",
    "AccountingDeleteVendorResponse": ".accounting_delete_vendor_response",
    "AccountingGetAccountResponse": ".accounting_get_account_response",
    "AccountingGetAccountsResponse": ".accounting_get_accounts_response",
    "AccountingGetExpenseResponse": ".accounting_get_expense_response",
    "AccountingGetExpensesResponse": ".accounting_get_expenses_response",
    "AccountingGetVendorResponse": ".accounting_get_vendor_response",
    "AccountingGetVendorsResponse": ".accounting_get_vendors_response",
    "AccountingProxyResponse": ".accounting_proxy_response",
    "AtsCreateOrUpdateCandidateRequest": ".ats_create_or_update_candidate_request",
    "AtsCreateOrUpdateCandidateResponse": ".ats_create_or_update_candidate_response",
    "AtsCreateOrUpdateDepartmentRequest": ".ats_create_or_update_department_request",
    "AtsCreateOrUpdateDepartmentResponse": ".ats_create_or_update_department_response",
    "AtsCreateOrUpdateJobRequest": ".ats_create_or_update_job_request",
    "AtsCreateOrUpdateJobResponse": ".ats_create_or_update_job_response",
    "AtsCreateOrUpdateOfferRequest": ".ats_create_or_update_offer_request",
    "AtsCreateOrUpdateOfferResponse": ".ats_create_or_update_offer_response",
    "AtsDeleteCandidateResponse": ".ats_delete_candidate_response",
    "AtsDeleteDepartmentResponse": ".ats_delete_department_response",
    "AtsDeleteJobResponse": ".ats_delete_job_response",
    "AtsDeleteOfferResponse": ".ats_delete_offer_response",
    "AtsGetCandidateResponse": ".ats_get_candidate_response",
    "AtsGetCandidatesResponse": ".ats_get_candidates_response",
    "AtsGetDepartmentResponse": ".ats_get_department_response",
    "AtsGetDepartmentsResponse": ".ats_get_departments_response",
    "AtsGetJobResponse": ".ats_get_job_response",
    "AtsGetJobsResponse": ".ats_get_jobs_response",
    "AtsGetOfferResponse": ".ats_get_offer_response",
    "AtsGetOffersResponse": ".ats_get_offers_response",
    "AtsProxyResponse": ".ats_proxy_response",
    "ChatCreateorUpdateMessageRequest": ".chat_createor_update_message_request",
    "ChatCreateorUpdateMessageResponse": ".chat_createor_update_message_response",
    "ChatGetChannelsResponse": ".chat_get_channels_response",
    "ChatGetUsersResponse": ".chat_get_users_response",
    "CommonAccount": ".common_account",
    "CommonAnalytics": ".common_analytics",
    "CommonApp": ".common_app",
    "CommonAppConfig": ".common_app_config",
    "CommonBaseError": ".common_base_error",
    "CommonChannel": ".common_channel",
    "CommonCommentTicket": ".common_comment_ticket",
    "CommonCommentTicketWrite": ".common_comment_ticket_write",
    "CommonCommonUnifiedFields": ".common_common_unified_fields",
    "CommonCompany": ".common_company",
    "CommonCompanyAddress": ".common_company_address",
    "CommonCompanyAssociation": ".common_company_association",
    "CommonConnectedApps": ".common_connected_apps",
    "CommonConnection": ".common_connection",
    "CommonContact": ".common_contact",
    "CommonContactAssociation": ".common_contact_association",
    "CommonContactRead": ".common_contact_read",
    "CommonContactWrite": ".common_contact_write",
    "CommonDeal": ".common_deal",
    "CommonDealAssociation": ".common_deal_association",
    "CommonDealRead": ".common_deal_read",
    "CommonDealWrite": ".common_deal_write",
    "CommonEnvironment": ".common_environment",
    "CommonEvent": ".common_event",
    "CommonEventAssociation": ".common_event_association",
    "CommonEventRead": ".common_event_read",
    "CommonEventWrite": ".common_event_write",
    "CommonLead": ".common_lead",
    "CommonLeadAssociation": ".common_lead_association",
    "CommonLeadRead": ".common_lead_read",
    "CommonLeadWrite": ".common_lead_write",
    "CommonMessage": ".common_message",
    "CommonNote": ".common_note",
    "CommonNoteAssociation": ".common_note_association",
    "CommonNoteRead": ".common_note_read",
    "CommonNoteWrite": ".common_note_write",
    "CommonRecentApiCalls": ".common_recent_api_calls",
    "CommonRecentConnections": ".common_recent_connections",
    "CommonResponseStatus": ".common_response_status",
    "CommonRevertUser": ".common_revert_user",
    "CommonStandardObject": ".common_standard_object",
    "CommonSummaryApiCalls": ".common_summary_api_calls",
    "CommonSvixAccount": ".common_svix_account",
    "CommonTask": ".common_task",
    "CommonTaskAssociation": ".common_task_association",
    "CommonTaskRead": ".common_task_read",
    "CommonTaskTicket": ".common_task_ticket",
    "CommonTaskTicketWrite": ".common_task_ticket_write",
    "CommonTaskWrite": ".common_task_write",
    "CommonTicketPriority": ".common_ticket_priority",
    "CommonTicketStatus": ".common_ticket_status",
    "CommonTpid": ".common_tpid",
    "CommonUser": ".common_user",
    "CommonUserAssociation": ".common_user_association",
    "CommonUserChat": ".common_user_chat",
    "CommonUserWrite": ".common_user_write",
    "ConnectionImport": ".connection_import",
    "ConnectionStatus": ".connection_status",
    "CreateAccountFieldMappingResponse": ".create_account_field_mapping_response",
    "CreateConnectionWebhookResponse": ".create_connection_webhook_response",
    "CreateFieldMappingResponse": ".create_field_mapping_response",
    "CrmCreateOrUpdateCompanyResponse": ".crm_create_or_update_company_response",
    "CrmCreateOrUpdateContactRequest": ".crm_create_or_update_contact_request",
    "CrmCreateOrUpdateContactResponse": ".crm_create_or_update_contact_response",
    "CrmCreateOrUpdateDealRequest": ".crm_create_or_update_deal_request",
    "CrmCreateOrUpdateDealResponse": ".crm_create_or_update_deal_response",
    "CrmCreateOrUpdateEventRequest": ".crm_create_or_update_event_request",
    "CrmCreateOrUpdateEventResponse": ".crm_create_or_update_event_response",
    "CrmCreateOrUpdateLeadRequest": ".crm_create_or_update_lead_request",
    "CrmCreateOrUpdateLeadResponse": ".crm_create_or_update_lead_response",
    "CrmCreateOrUpdateNoteRequest": ".crm_create_or_update_note_request",
    "CrmCreateOrUpdateNoteResponse": ".crm_create_or_update_note_response",
    "CrmCreateOrUpdateTaskRequest": ".crm_create_or_update_task_request",
    "CrmCreateOrUpdateTaskResponse": ".crm_create_or_update_task_response",
    "CrmCreateOrUpdateUserResponse": ".crm_create_or_update_user_response",
    "CrmDeleteEventResponse": ".crm_delete_event_response",
    "CrmFieldDetailsType": ".crm_field_details_type",
    "CrmFieldDetailsTypeRead": ".crm_field_details_type_read",
    "CrmFieldDetailsTypeRequest": ".crm_field_details_type_request",
    "CrmGetCompaniesResponse": ".crm_get_companies_response",
    "CrmGetCompanyResponse": ".crm_get_company_response",
    "CrmGetContactResponse": ".crm_get_contact_response",
    "CrmGetContactsResponse": ".crm_get_contacts_response",
    "CrmGetDealResponse": ".crm_get_deal_response",
    "CrmGetDealsResponse": ".crm_get_deals_response",
    "CrmGetEventResponse": ".crm_get_event_response",
    "CrmGetEventsResponse": ".crm_get_events_response",
    "CrmGetLeadResponse": ".crm_get_lead_response",
    "CrmGetLeadsResponse": ".crm_get_leads_response",
    "CrmGetNoteResponse": ".crm_get_note_response",
    "CrmGetNotesResponse": ".crm_get_notes_response",
    "CrmGetObjectPropertiesResponse": ".crm_get_object_properties_response",
    "CrmGetTaskResponse": ".crm_get_task_response",
    "CrmGetTasksResponse": ".crm_get_tasks_response",
    "CrmGetUserResponse": ".crm_get_user_response",
    "CrmGetUsersResponse": ".crm_get_users_response",
    "CrmMetadata": ".crm_metadata",
    "CrmMetadataResponse": ".crm_metadata_response",
    "CrmProxyResponse": ".crm_proxy_response",
    "CrmSearchCompaniesResponse": ".crm_search_companies_response",
    "CrmSearchContactsResponse": ".crm_search_contacts_response",
    "CrmSearchDealsResponse": ".crm_search_deals_response",
    "CrmSearchEventsResponse": ".crm_search_events_response",
    "CrmSearchLeadsResponse": ".crm_search_leads_response",
    "CrmSearchNotesResponse": ".crm_search_notes_response",
    "CrmSearchTasksResponse": ".crm_search_tasks_response",
    "CrmSearchUsersResponse": ".crm_search_users_response",
    "CrmSetObjectPropertiesRequest": ".crm_set_object_properties_request",
    "CrmSetObjectPropertiesResponse": ".crm_set_object_properties_response",
    "CrmStatus": ".crm_status",
    "DeleteAccountFieldMappingConfigResponse": ".delete_account_field_mapping_config_response",
    "DeleteConnectionResponse": ".delete_connection_response",
    "DeleteConnectionWebhookResponse": ".delete_connection_webhook_response",
    "DeleteFieldMappingResponse": ".delete_field_mapping_response",
    "FieldMappingType": ".field_mapping_type",
    "GetAllConnectionResponse": ".get_all_connection_response",
    "GetConnectStatusResponse": ".get_connect_status_response",
    "GetConnectionResponse": ".get_connection_response",
    "GetConnectionWebhookResponse": ".get_connection_webhook_response",
    "GetFieldMappingConfigResponse": ".get_field_mapping_config_response",
    "GetFieldMappingsResponse": ".get_field_mappings_response",
    "ImportConnectionsResponse": ".import_connections_response",
    "InternalCreateTelemetryEntryResponse": ".internal_create_telemetry_entry_response",
    "InternalDeleteRevertAppResponse": ".internal_delete_revert_app_response",
    "InternalGetAccountDetailsResponse": ".internal_get_account_details_response",
    "InternalGetAnalyticsResponse": ".internal_get_analytics_response",
    "InternalRecentApiCalls": ".internal_recent_api_calls",
    "InternalRecentAppApiCallsResponse": ".internal_recent_app_api_calls_response",
    "InternalSvixAccountResponse": ".internal_svix_account_response",
    "InternalSvixMagicLinkResponse": ".internal_svix_magic_link_response",
    "InternalsetOnboardingResponse": ".internalset_onboarding_response",
    "MappableFieldType": ".mappable_field_type",
    "TicketCreateOrUpdateCommentRequest": ".ticket_create_or_update_comment_request",
    "TicketCreateOrUpdateCommentResponse": ".ticket_create_or_update_comment_response",
    "TicketCreateOrUpdateTaskRequest": ".ticket_create_or_update_task_request",
    "TicketCreateOrUpdateTaskResponse": ".ticket_create_or_update_task_response",
    "TicketGetCollectionsResponse": ".ticket_get_collections_response",
    "TicketGetCommentResponse": ".ticket_get_comment_response",
    "TicketGetCommentsResponse": ".ticket_get_comments_response",
    "TicketGetTaskResponse": ".ticket_get_task_response",
    "TicketGetTasksResponse": ".ticket_get_tasks_response",
    "TicketGetUserResponse": ".ticket_get_user_response",
    "TicketGetUsersResponse": ".ticket_get_users_response",
    "TicketProxyResponse": ".ticket_proxy_response",
    "TriggerSyncResponse": ".trigger_sync_response",
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
    "AccountingCreateOrUpdateAccountRequest",
    "AccountingCreateOrUpdateAccountResponse",
    "AccountingCreateOrUpdateExpenseRequest",
    "AccountingCreateOrUpdateExpenseResponse",
    "AccountingCreateOrUpdateVendorRequest",
    "AccountingCreateOrUpdateVendorResponse",
    "AccountingDeleteAccountResponse",
    "AccountingDeleteExpenseResponse",
    "AccountingDeleteVendorResponse",
    "AccountingGetAccountResponse",
    "AccountingGetAccountsResponse",
    "AccountingGetExpenseResponse",
    "AccountingGetExpensesResponse",
    "AccountingGetVendorResponse",
    "AccountingGetVendorsResponse",
    "AccountingProxyResponse",
    "AtsCreateOrUpdateCandidateRequest",
    "AtsCreateOrUpdateCandidateResponse",
    "AtsCreateOrUpdateDepartmentRequest",
    "AtsCreateOrUpdateDepartmentResponse",
    "AtsCreateOrUpdateJobRequest",
    "AtsCreateOrUpdateJobResponse",
    "AtsCreateOrUpdateOfferRequest",
    "AtsCreateOrUpdateOfferResponse",
    "AtsDeleteCandidateResponse",
    "AtsDeleteDepartmentResponse",
    "AtsDeleteJobResponse",
    "AtsDeleteOfferResponse",
    "AtsGetCandidateResponse",
    "AtsGetCandidatesResponse",
    "AtsGetDepartmentResponse",
    "AtsGetDepartmentsResponse",
    "AtsGetJobResponse",
    "AtsGetJobsResponse",
    "AtsGetOfferResponse",
    "AtsGetOffersResponse",
    "AtsProxyResponse",
    "ChatCreateorUpdateMessageRequest",
    "ChatCreateorUpdateMessageResponse",
    "ChatGetChannelsResponse",
    "ChatGetUsersResponse",
    "CommonAccount",
    "CommonAnalytics",
    "CommonApp",
    "CommonAppConfig",
    "CommonBaseError",
    "CommonChannel",
    "CommonCommentTicket",
    "CommonCommentTicketWrite",
    "CommonCommonUnifiedFields",
    "CommonCompany",
    "CommonCompanyAddress",
    "CommonCompanyAssociation",
    "CommonConnectedApps",
    "CommonConnection",
    "CommonContact",
    "CommonContactAssociation",
    "CommonContactRead",
    "CommonContactWrite",
    "CommonDeal",
    "CommonDealAssociation",
    "CommonDealRead",
    "CommonDealWrite",
    "CommonEnvironment",
    "CommonEvent",
    "CommonEventAssociation",
    "CommonEventRead",
    "CommonEventWrite",
    "CommonLead",
    "CommonLeadAssociation",
    "CommonLeadRead",
    "CommonLeadWrite",
    "CommonMessage",
    "CommonNote",
    "CommonNoteAssociation",
    "CommonNoteRead",
    "CommonNoteWrite",
    "CommonRecentApiCalls",
    "CommonRecentConnections",
    "CommonResponseStatus",
    "CommonRevertUser",
    "CommonStandardObject",
    "CommonSummaryApiCalls",
    "CommonSvixAccount",
    "CommonTask",
    "CommonTaskAssociation",
    "CommonTaskRead",
    "CommonTaskTicket",
    "CommonTaskTicketWrite",
    "CommonTaskWrite",
    "CommonTicketPriority",
    "CommonTicketStatus",
    "CommonTpid",
    "CommonUser",
    "CommonUserAssociation",
    "CommonUserChat",
    "CommonUserWrite",
    "ConnectionImport",
    "ConnectionStatus",
    "CreateAccountFieldMappingResponse",
    "CreateConnectionWebhookResponse",
    "CreateFieldMappingResponse",
    "CrmCreateOrUpdateCompanyResponse",
    "CrmCreateOrUpdateContactRequest",
    "CrmCreateOrUpdateContactResponse",
    "CrmCreateOrUpdateDealRequest",
    "CrmCreateOrUpdateDealResponse",
    "CrmCreateOrUpdateEventRequest",
    "CrmCreateOrUpdateEventResponse",
    "CrmCreateOrUpdateLeadRequest",
    "CrmCreateOrUpdateLeadResponse",
    "CrmCreateOrUpdateNoteRequest",
    "CrmCreateOrUpdateNoteResponse",
    "CrmCreateOrUpdateTaskRequest",
    "CrmCreateOrUpdateTaskResponse",
    "CrmCreateOrUpdateUserResponse",
    "CrmDeleteEventResponse",
    "CrmFieldDetailsType",
    "CrmFieldDetailsTypeRead",
    "CrmFieldDetailsTypeRequest",
    "CrmGetCompaniesResponse",
    "CrmGetCompanyResponse",
    "CrmGetContactResponse",
    "CrmGetContactsResponse",
    "CrmGetDealResponse",
    "CrmGetDealsResponse",
    "CrmGetEventResponse",
    "CrmGetEventsResponse",
    "CrmGetLeadResponse",
    "CrmGetLeadsResponse",
    "CrmGetNoteResponse",
    "CrmGetNotesResponse",
    "CrmGetObjectPropertiesResponse",
    "CrmGetTaskResponse",
    "CrmGetTasksResponse",
    "CrmGetUserResponse",
    "CrmGetUsersResponse",
    "CrmMetadata",
    "CrmMetadataResponse",
    "CrmProxyResponse",
    "CrmSearchCompaniesResponse",
    "CrmSearchContactsResponse",
    "CrmSearchDealsResponse",
    "CrmSearchEventsResponse",
    "CrmSearchLeadsResponse",
    "CrmSearchNotesResponse",
    "CrmSearchTasksResponse",
    "CrmSearchUsersResponse",
    "CrmSetObjectPropertiesRequest",
    "CrmSetObjectPropertiesResponse",
    "CrmStatus",
    "DeleteAccountFieldMappingConfigResponse",
    "DeleteConnectionResponse",
    "DeleteConnectionWebhookResponse",
    "DeleteFieldMappingResponse",
    "FieldMappingType",
    "GetAllConnectionResponse",
    "GetConnectStatusResponse",
    "GetConnectionResponse",
    "GetConnectionWebhookResponse",
    "GetFieldMappingConfigResponse",
    "GetFieldMappingsResponse",
    "ImportConnectionsResponse",
    "InternalCreateTelemetryEntryResponse",
    "InternalDeleteRevertAppResponse",
    "InternalGetAccountDetailsResponse",
    "InternalGetAnalyticsResponse",
    "InternalRecentApiCalls",
    "InternalRecentAppApiCallsResponse",
    "InternalSvixAccountResponse",
    "InternalSvixMagicLinkResponse",
    "InternalsetOnboardingResponse",
    "MappableFieldType",
    "TicketCreateOrUpdateCommentRequest",
    "TicketCreateOrUpdateCommentResponse",
    "TicketCreateOrUpdateTaskRequest",
    "TicketCreateOrUpdateTaskResponse",
    "TicketGetCollectionsResponse",
    "TicketGetCommentResponse",
    "TicketGetCommentsResponse",
    "TicketGetTaskResponse",
    "TicketGetTasksResponse",
    "TicketGetUserResponse",
    "TicketGetUsersResponse",
    "TicketProxyResponse",
    "TriggerSyncResponse",
]
