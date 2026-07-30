



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_type import AddressType
    from .anonymized import Anonymized
    from .applicant import Applicant
    from .applicant_social_links_item import ApplicantSocialLinksItem
    from .applicant_websites_item import ApplicantWebsitesItem
    from .applicant_websites_item_type import ApplicantWebsitesItemType
    from .applicants_filter import ApplicantsFilter
    from .archived import Archived
    from .ats_activity import AtsActivity
    from .ats_event_type import AtsEventType
    from .ats_webhook_event import AtsWebhookEvent
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .code import Code
    from .create_applicant_response import CreateApplicantResponse
    from .create_job_response import CreateJobResponse
    from .created_at import CreatedAt
    from .created_by import CreatedBy
    from .currency import Currency
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .delete_job_response import DeleteJobResponse
    from .deleted import Deleted
    from .deleted_at import DeletedAt
    from .deleted_by import DeletedBy
    from .department import Department
    from .description import Description
    from .email import Email
    from .email_type import EmailType
    from .get_applicant_response import GetApplicantResponse
    from .get_applicants_response import GetApplicantsResponse
    from .get_job_response import GetJobResponse
    from .get_jobs_response import GetJobsResponse
    from .id import Id
    from .initials import Initials
    from .job import Job
    from .job_blocks_item import JobBlocksItem
    from .job_branch import JobBranch
    from .job_employment_terms import JobEmploymentTerms
    from .job_hiring_managers_item import JobHiringManagersItem
    from .job_salary import JobSalary
    from .job_status import JobStatus
    from .job_visibility import JobVisibility
    from .jobs_filter import JobsFilter
    from .language import Language
    from .last_interaction_at import LastInteractionAt
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .offer import Offer
    from .owner_id import OwnerId
    from .payment_required_response import PaymentRequiredResponse
    from .phone_number import PhoneNumber
    from .phone_number_type import PhoneNumberType
    from .published_at import PublishedAt
    from .record_url import RecordUrl
    from .row_version import RowVersion
    from .tags import Tags
    from .title import Title
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_job_response import UpdateJobResponse
    from .updated_at import UpdatedAt
    from .updated_by import UpdatedBy
    from .url import Url
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressType": ".address_type",
    "Anonymized": ".anonymized",
    "Applicant": ".applicant",
    "ApplicantSocialLinksItem": ".applicant_social_links_item",
    "ApplicantWebsitesItem": ".applicant_websites_item",
    "ApplicantWebsitesItemType": ".applicant_websites_item_type",
    "ApplicantsFilter": ".applicants_filter",
    "Archived": ".archived",
    "AtsActivity": ".ats_activity",
    "AtsEventType": ".ats_event_type",
    "AtsWebhookEvent": ".ats_webhook_event",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "Code": ".code",
    "CreateApplicantResponse": ".create_applicant_response",
    "CreateJobResponse": ".create_job_response",
    "CreatedAt": ".created_at",
    "CreatedBy": ".created_by",
    "Currency": ".currency",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "DeleteJobResponse": ".delete_job_response",
    "Deleted": ".deleted",
    "DeletedAt": ".deleted_at",
    "DeletedBy": ".deleted_by",
    "Department": ".department",
    "Description": ".description",
    "Email": ".email",
    "EmailType": ".email_type",
    "GetApplicantResponse": ".get_applicant_response",
    "GetApplicantsResponse": ".get_applicants_response",
    "GetJobResponse": ".get_job_response",
    "GetJobsResponse": ".get_jobs_response",
    "Id": ".id",
    "Initials": ".initials",
    "Job": ".job",
    "JobBlocksItem": ".job_blocks_item",
    "JobBranch": ".job_branch",
    "JobEmploymentTerms": ".job_employment_terms",
    "JobHiringManagersItem": ".job_hiring_managers_item",
    "JobSalary": ".job_salary",
    "JobStatus": ".job_status",
    "JobVisibility": ".job_visibility",
    "JobsFilter": ".jobs_filter",
    "Language": ".language",
    "LastInteractionAt": ".last_interaction_at",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "Offer": ".offer",
    "OwnerId": ".owner_id",
    "PaymentRequiredResponse": ".payment_required_response",
    "PhoneNumber": ".phone_number",
    "PhoneNumberType": ".phone_number_type",
    "PublishedAt": ".published_at",
    "RecordUrl": ".record_url",
    "RowVersion": ".row_version",
    "Tags": ".tags",
    "Title": ".title",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateJobResponse": ".update_job_response",
    "UpdatedAt": ".updated_at",
    "UpdatedBy": ".updated_by",
    "Url": ".url",
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
    "Address",
    "AddressType",
    "Anonymized",
    "Applicant",
    "ApplicantSocialLinksItem",
    "ApplicantWebsitesItem",
    "ApplicantWebsitesItemType",
    "ApplicantsFilter",
    "Archived",
    "AtsActivity",
    "AtsEventType",
    "AtsWebhookEvent",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "Code",
    "CreateApplicantResponse",
    "CreateJobResponse",
    "CreatedAt",
    "CreatedBy",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "DeleteJobResponse",
    "Deleted",
    "DeletedAt",
    "DeletedBy",
    "Department",
    "Description",
    "Email",
    "EmailType",
    "GetApplicantResponse",
    "GetApplicantsResponse",
    "GetJobResponse",
    "GetJobsResponse",
    "Id",
    "Initials",
    "Job",
    "JobBlocksItem",
    "JobBranch",
    "JobEmploymentTerms",
    "JobHiringManagersItem",
    "JobSalary",
    "JobStatus",
    "JobVisibility",
    "JobsFilter",
    "Language",
    "LastInteractionAt",
    "Links",
    "Meta",
    "MetaCursors",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "Offer",
    "OwnerId",
    "PaymentRequiredResponse",
    "PhoneNumber",
    "PhoneNumberType",
    "PublishedAt",
    "RecordUrl",
    "RowVersion",
    "Tags",
    "Title",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateJobResponse",
    "UpdatedAt",
    "UpdatedBy",
    "Url",
]
