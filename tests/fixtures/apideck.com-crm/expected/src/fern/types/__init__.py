



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .activities_filter import ActivitiesFilter
    from .activity import Activity
    from .activity_attendee import ActivityAttendee
    from .activity_attendee_status import ActivityAttendeeStatus
    from .activity_show_as import ActivityShowAs
    from .activity_type import ActivityType
    from .address import Address
    from .address_type import AddressType
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .bank_account import BankAccount
    from .bank_account_account_type import BankAccountAccountType
    from .companies_filter import CompaniesFilter
    from .companies_sort import CompaniesSort
    from .companies_sort_by import CompaniesSortBy
    from .company import Company
    from .company_row_type import CompanyRowType
    from .contact import Contact
    from .contact_gender import ContactGender
    from .contact_type import ContactType
    from .contacts_filter import ContactsFilter
    from .contacts_sort import ContactsSort
    from .contacts_sort_by import ContactsSortBy
    from .create_activity_response import CreateActivityResponse
    from .create_company_response import CreateCompanyResponse
    from .create_contact_response import CreateContactResponse
    from .create_lead_response import CreateLeadResponse
    from .create_note_response import CreateNoteResponse
    from .create_opportunity_response import CreateOpportunityResponse
    from .create_pipeline_response import CreatePipelineResponse
    from .create_user_response import CreateUserResponse
    from .crm_event_type import CrmEventType
    from .crm_webhook_event import CrmWebhookEvent
    from .currency import Currency
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .delete_activity_response import DeleteActivityResponse
    from .delete_company_response import DeleteCompanyResponse
    from .delete_contact_response import DeleteContactResponse
    from .delete_lead_response import DeleteLeadResponse
    from .delete_note_response import DeleteNoteResponse
    from .delete_opportunity_response import DeleteOpportunityResponse
    from .delete_pipeline_response import DeletePipelineResponse
    from .delete_user_response import DeleteUserResponse
    from .email import Email
    from .email_type import EmailType
    from .first_name import FirstName
    from .get_activities_response import GetActivitiesResponse
    from .get_activity_response import GetActivityResponse
    from .get_companies_response import GetCompaniesResponse
    from .get_company_response import GetCompanyResponse
    from .get_contact_response import GetContactResponse
    from .get_contacts_response import GetContactsResponse
    from .get_lead_response import GetLeadResponse
    from .get_leads_response import GetLeadsResponse
    from .get_note_response import GetNoteResponse
    from .get_notes_response import GetNotesResponse
    from .get_opportunities_response import GetOpportunitiesResponse
    from .get_opportunity_response import GetOpportunityResponse
    from .get_pipeline_response import GetPipelineResponse
    from .get_pipelines_response import GetPipelinesResponse
    from .get_user_response import GetUserResponse
    from .get_users_response import GetUsersResponse
    from .last_name import LastName
    from .lead import Lead
    from .leads_filter import LeadsFilter
    from .leads_sort import LeadsSort
    from .leads_sort_by import LeadsSortBy
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .note import Note
    from .opportunities_filter import OpportunitiesFilter
    from .opportunities_sort import OpportunitiesSort
    from .opportunities_sort_by import OpportunitiesSortBy
    from .opportunity import Opportunity
    from .payment_required_response import PaymentRequiredResponse
    from .phone_number import PhoneNumber
    from .phone_number_type import PhoneNumberType
    from .pipeline import Pipeline
    from .pipeline_stages_item import PipelineStagesItem
    from .row_version import RowVersion
    from .social_link import SocialLink
    from .sort_direction import SortDirection
    from .tags import Tags
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_activity_response import UpdateActivityResponse
    from .update_company_response import UpdateCompanyResponse
    from .update_contact_response import UpdateContactResponse
    from .update_lead_response import UpdateLeadResponse
    from .update_note_response import UpdateNoteResponse
    from .update_opportunity_response import UpdateOpportunityResponse
    from .update_pipeline_response import UpdatePipelineResponse
    from .update_user_response import UpdateUserResponse
    from .user import User
    from .website import Website
    from .website_type import WebsiteType
_dynamic_imports: typing.Dict[str, str] = {
    "ActivitiesFilter": ".activities_filter",
    "Activity": ".activity",
    "ActivityAttendee": ".activity_attendee",
    "ActivityAttendeeStatus": ".activity_attendee_status",
    "ActivityShowAs": ".activity_show_as",
    "ActivityType": ".activity_type",
    "Address": ".address",
    "AddressType": ".address_type",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "BankAccount": ".bank_account",
    "BankAccountAccountType": ".bank_account_account_type",
    "CompaniesFilter": ".companies_filter",
    "CompaniesSort": ".companies_sort",
    "CompaniesSortBy": ".companies_sort_by",
    "Company": ".company",
    "CompanyRowType": ".company_row_type",
    "Contact": ".contact",
    "ContactGender": ".contact_gender",
    "ContactType": ".contact_type",
    "ContactsFilter": ".contacts_filter",
    "ContactsSort": ".contacts_sort",
    "ContactsSortBy": ".contacts_sort_by",
    "CreateActivityResponse": ".create_activity_response",
    "CreateCompanyResponse": ".create_company_response",
    "CreateContactResponse": ".create_contact_response",
    "CreateLeadResponse": ".create_lead_response",
    "CreateNoteResponse": ".create_note_response",
    "CreateOpportunityResponse": ".create_opportunity_response",
    "CreatePipelineResponse": ".create_pipeline_response",
    "CreateUserResponse": ".create_user_response",
    "CrmEventType": ".crm_event_type",
    "CrmWebhookEvent": ".crm_webhook_event",
    "Currency": ".currency",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "DeleteActivityResponse": ".delete_activity_response",
    "DeleteCompanyResponse": ".delete_company_response",
    "DeleteContactResponse": ".delete_contact_response",
    "DeleteLeadResponse": ".delete_lead_response",
    "DeleteNoteResponse": ".delete_note_response",
    "DeleteOpportunityResponse": ".delete_opportunity_response",
    "DeletePipelineResponse": ".delete_pipeline_response",
    "DeleteUserResponse": ".delete_user_response",
    "Email": ".email",
    "EmailType": ".email_type",
    "FirstName": ".first_name",
    "GetActivitiesResponse": ".get_activities_response",
    "GetActivityResponse": ".get_activity_response",
    "GetCompaniesResponse": ".get_companies_response",
    "GetCompanyResponse": ".get_company_response",
    "GetContactResponse": ".get_contact_response",
    "GetContactsResponse": ".get_contacts_response",
    "GetLeadResponse": ".get_lead_response",
    "GetLeadsResponse": ".get_leads_response",
    "GetNoteResponse": ".get_note_response",
    "GetNotesResponse": ".get_notes_response",
    "GetOpportunitiesResponse": ".get_opportunities_response",
    "GetOpportunityResponse": ".get_opportunity_response",
    "GetPipelineResponse": ".get_pipeline_response",
    "GetPipelinesResponse": ".get_pipelines_response",
    "GetUserResponse": ".get_user_response",
    "GetUsersResponse": ".get_users_response",
    "LastName": ".last_name",
    "Lead": ".lead",
    "LeadsFilter": ".leads_filter",
    "LeadsSort": ".leads_sort",
    "LeadsSortBy": ".leads_sort_by",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "Note": ".note",
    "OpportunitiesFilter": ".opportunities_filter",
    "OpportunitiesSort": ".opportunities_sort",
    "OpportunitiesSortBy": ".opportunities_sort_by",
    "Opportunity": ".opportunity",
    "PaymentRequiredResponse": ".payment_required_response",
    "PhoneNumber": ".phone_number",
    "PhoneNumberType": ".phone_number_type",
    "Pipeline": ".pipeline",
    "PipelineStagesItem": ".pipeline_stages_item",
    "RowVersion": ".row_version",
    "SocialLink": ".social_link",
    "SortDirection": ".sort_direction",
    "Tags": ".tags",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateActivityResponse": ".update_activity_response",
    "UpdateCompanyResponse": ".update_company_response",
    "UpdateContactResponse": ".update_contact_response",
    "UpdateLeadResponse": ".update_lead_response",
    "UpdateNoteResponse": ".update_note_response",
    "UpdateOpportunityResponse": ".update_opportunity_response",
    "UpdatePipelineResponse": ".update_pipeline_response",
    "UpdateUserResponse": ".update_user_response",
    "User": ".user",
    "Website": ".website",
    "WebsiteType": ".website_type",
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
    "ActivitiesFilter",
    "Activity",
    "ActivityAttendee",
    "ActivityAttendeeStatus",
    "ActivityShowAs",
    "ActivityType",
    "Address",
    "AddressType",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "BankAccount",
    "BankAccountAccountType",
    "CompaniesFilter",
    "CompaniesSort",
    "CompaniesSortBy",
    "Company",
    "CompanyRowType",
    "Contact",
    "ContactGender",
    "ContactType",
    "ContactsFilter",
    "ContactsSort",
    "ContactsSortBy",
    "CreateActivityResponse",
    "CreateCompanyResponse",
    "CreateContactResponse",
    "CreateLeadResponse",
    "CreateNoteResponse",
    "CreateOpportunityResponse",
    "CreatePipelineResponse",
    "CreateUserResponse",
    "CrmEventType",
    "CrmWebhookEvent",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "DeleteActivityResponse",
    "DeleteCompanyResponse",
    "DeleteContactResponse",
    "DeleteLeadResponse",
    "DeleteNoteResponse",
    "DeleteOpportunityResponse",
    "DeletePipelineResponse",
    "DeleteUserResponse",
    "Email",
    "EmailType",
    "FirstName",
    "GetActivitiesResponse",
    "GetActivityResponse",
    "GetCompaniesResponse",
    "GetCompanyResponse",
    "GetContactResponse",
    "GetContactsResponse",
    "GetLeadResponse",
    "GetLeadsResponse",
    "GetNoteResponse",
    "GetNotesResponse",
    "GetOpportunitiesResponse",
    "GetOpportunityResponse",
    "GetPipelineResponse",
    "GetPipelinesResponse",
    "GetUserResponse",
    "GetUsersResponse",
    "LastName",
    "Lead",
    "LeadsFilter",
    "LeadsSort",
    "LeadsSortBy",
    "Links",
    "Meta",
    "MetaCursors",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "Note",
    "OpportunitiesFilter",
    "OpportunitiesSort",
    "OpportunitiesSortBy",
    "Opportunity",
    "PaymentRequiredResponse",
    "PhoneNumber",
    "PhoneNumberType",
    "Pipeline",
    "PipelineStagesItem",
    "RowVersion",
    "SocialLink",
    "SortDirection",
    "Tags",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateActivityResponse",
    "UpdateCompanyResponse",
    "UpdateContactResponse",
    "UpdateLeadResponse",
    "UpdateNoteResponse",
    "UpdateOpportunityResponse",
    "UpdatePipelineResponse",
    "UpdateUserResponse",
    "User",
    "Website",
    "WebsiteType",
]
