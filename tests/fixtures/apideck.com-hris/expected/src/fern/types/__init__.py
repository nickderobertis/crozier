



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_type import AddressType
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .benefit import Benefit
    from .company_id import CompanyId
    from .company_name import CompanyName
    from .compensation import Compensation
    from .create_department_response import CreateDepartmentResponse
    from .create_employee_response import CreateEmployeeResponse
    from .create_hris_company_response import CreateHrisCompanyResponse
    from .create_time_off_request_response import CreateTimeOffRequestResponse
    from .created_at import CreatedAt
    from .created_by import CreatedBy
    from .currency import Currency
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .deduction import Deduction
    from .delete_department_response import DeleteDepartmentResponse
    from .delete_employee_response import DeleteEmployeeResponse
    from .delete_hris_company_response import DeleteHrisCompanyResponse
    from .delete_time_off_request_response import DeleteTimeOffRequestResponse
    from .department import Department
    from .description import Description
    from .division import Division
    from .email import Email
    from .email_type import EmailType
    from .employee import Employee
    from .employee_compensations_item import EmployeeCompensationsItem
    from .employee_compensations_item_flsa_status import EmployeeCompensationsItemFlsaStatus
    from .employee_employment_role import EmployeeEmploymentRole
    from .employee_employment_role_sub_type import EmployeeEmploymentRoleSubType
    from .employee_employment_role_type import EmployeeEmploymentRoleType
    from .employee_jobs_item import EmployeeJobsItem
    from .employee_leaving_reason import EmployeeLeavingReason
    from .employee_manager import EmployeeManager
    from .employee_number import EmployeeNumber
    from .employee_partner import EmployeePartner
    from .employee_payroll import EmployeePayroll
    from .employee_payrolls import EmployeePayrolls
    from .employee_schedules import EmployeeSchedules
    from .employee_social_links_item import EmployeeSocialLinksItem
    from .employee_team import EmployeeTeam
    from .employees_filter import EmployeesFilter
    from .employees_filter_employment_status import EmployeesFilterEmploymentStatus
    from .employees_sort import EmployeesSort
    from .employees_sort_by import EmployeesSortBy
    from .employment_status import EmploymentStatus
    from .first_name import FirstName
    from .gender import Gender
    from .get_department_response import GetDepartmentResponse
    from .get_departments_response import GetDepartmentsResponse
    from .get_employee_payroll_response import GetEmployeePayrollResponse
    from .get_employee_payrolls_response import GetEmployeePayrollsResponse
    from .get_employee_response import GetEmployeeResponse
    from .get_employee_schedules_response import GetEmployeeSchedulesResponse
    from .get_employees_response import GetEmployeesResponse
    from .get_hris_companies_response import GetHrisCompaniesResponse
    from .get_hris_company_response import GetHrisCompanyResponse
    from .get_hris_job_response import GetHrisJobResponse
    from .get_hris_jobs_response import GetHrisJobsResponse
    from .get_payroll_response import GetPayrollResponse
    from .get_payrolls_response import GetPayrollsResponse
    from .get_time_off_request_response import GetTimeOffRequestResponse
    from .get_time_off_requests_response import GetTimeOffRequestsResponse
    from .hris_company import HrisCompany
    from .hris_company_status import HrisCompanyStatus
    from .hris_event_type import HrisEventType
    from .hris_job import HrisJob
    from .hris_job_location import HrisJobLocation
    from .hris_jobs import HrisJobs
    from .id import Id
    from .language import Language
    from .last_name import LastName
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .middle_name import MiddleName
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .payment_required_response import PaymentRequiredResponse
    from .payment_unit import PaymentUnit
    from .payroll import Payroll
    from .payroll_totals import PayrollTotals
    from .payrolls_filter import PayrollsFilter
    from .phone_number import PhoneNumber
    from .phone_number_type import PhoneNumberType
    from .photo_url import PhotoUrl
    from .row_version import RowVersion
    from .schedule import Schedule
    from .schedule_work_pattern import ScheduleWorkPattern
    from .schedule_work_pattern_even_weeks import ScheduleWorkPatternEvenWeeks
    from .schedule_work_pattern_odd_weeks import ScheduleWorkPatternOddWeeks
    from .sort_direction import SortDirection
    from .tax import Tax
    from .time_off_request import TimeOffRequest
    from .time_off_request_notes import TimeOffRequestNotes
    from .time_off_request_request_type import TimeOffRequestRequestType
    from .time_off_request_status import TimeOffRequestStatus
    from .time_off_request_units import TimeOffRequestUnits
    from .time_off_requests_filter import TimeOffRequestsFilter
    from .time_off_requests_filter_time_off_request_status import TimeOffRequestsFilterTimeOffRequestStatus
    from .title import Title
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_department_response import UpdateDepartmentResponse
    from .update_employee_response import UpdateEmployeeResponse
    from .update_hris_company_response import UpdateHrisCompanyResponse
    from .update_time_off_request_response import UpdateTimeOffRequestResponse
    from .updated_at import UpdatedAt
    from .updated_by import UpdatedBy
    from .webhook_event import WebhookEvent
    from .website import Website
    from .website_type import WebsiteType
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressType": ".address_type",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "Benefit": ".benefit",
    "CompanyId": ".company_id",
    "CompanyName": ".company_name",
    "Compensation": ".compensation",
    "CreateDepartmentResponse": ".create_department_response",
    "CreateEmployeeResponse": ".create_employee_response",
    "CreateHrisCompanyResponse": ".create_hris_company_response",
    "CreateTimeOffRequestResponse": ".create_time_off_request_response",
    "CreatedAt": ".created_at",
    "CreatedBy": ".created_by",
    "Currency": ".currency",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "Deduction": ".deduction",
    "DeleteDepartmentResponse": ".delete_department_response",
    "DeleteEmployeeResponse": ".delete_employee_response",
    "DeleteHrisCompanyResponse": ".delete_hris_company_response",
    "DeleteTimeOffRequestResponse": ".delete_time_off_request_response",
    "Department": ".department",
    "Description": ".description",
    "Division": ".division",
    "Email": ".email",
    "EmailType": ".email_type",
    "Employee": ".employee",
    "EmployeeCompensationsItem": ".employee_compensations_item",
    "EmployeeCompensationsItemFlsaStatus": ".employee_compensations_item_flsa_status",
    "EmployeeEmploymentRole": ".employee_employment_role",
    "EmployeeEmploymentRoleSubType": ".employee_employment_role_sub_type",
    "EmployeeEmploymentRoleType": ".employee_employment_role_type",
    "EmployeeJobsItem": ".employee_jobs_item",
    "EmployeeLeavingReason": ".employee_leaving_reason",
    "EmployeeManager": ".employee_manager",
    "EmployeeNumber": ".employee_number",
    "EmployeePartner": ".employee_partner",
    "EmployeePayroll": ".employee_payroll",
    "EmployeePayrolls": ".employee_payrolls",
    "EmployeeSchedules": ".employee_schedules",
    "EmployeeSocialLinksItem": ".employee_social_links_item",
    "EmployeeTeam": ".employee_team",
    "EmployeesFilter": ".employees_filter",
    "EmployeesFilterEmploymentStatus": ".employees_filter_employment_status",
    "EmployeesSort": ".employees_sort",
    "EmployeesSortBy": ".employees_sort_by",
    "EmploymentStatus": ".employment_status",
    "FirstName": ".first_name",
    "Gender": ".gender",
    "GetDepartmentResponse": ".get_department_response",
    "GetDepartmentsResponse": ".get_departments_response",
    "GetEmployeePayrollResponse": ".get_employee_payroll_response",
    "GetEmployeePayrollsResponse": ".get_employee_payrolls_response",
    "GetEmployeeResponse": ".get_employee_response",
    "GetEmployeeSchedulesResponse": ".get_employee_schedules_response",
    "GetEmployeesResponse": ".get_employees_response",
    "GetHrisCompaniesResponse": ".get_hris_companies_response",
    "GetHrisCompanyResponse": ".get_hris_company_response",
    "GetHrisJobResponse": ".get_hris_job_response",
    "GetHrisJobsResponse": ".get_hris_jobs_response",
    "GetPayrollResponse": ".get_payroll_response",
    "GetPayrollsResponse": ".get_payrolls_response",
    "GetTimeOffRequestResponse": ".get_time_off_request_response",
    "GetTimeOffRequestsResponse": ".get_time_off_requests_response",
    "HrisCompany": ".hris_company",
    "HrisCompanyStatus": ".hris_company_status",
    "HrisEventType": ".hris_event_type",
    "HrisJob": ".hris_job",
    "HrisJobLocation": ".hris_job_location",
    "HrisJobs": ".hris_jobs",
    "Id": ".id",
    "Language": ".language",
    "LastName": ".last_name",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "MiddleName": ".middle_name",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "PaymentRequiredResponse": ".payment_required_response",
    "PaymentUnit": ".payment_unit",
    "Payroll": ".payroll",
    "PayrollTotals": ".payroll_totals",
    "PayrollsFilter": ".payrolls_filter",
    "PhoneNumber": ".phone_number",
    "PhoneNumberType": ".phone_number_type",
    "PhotoUrl": ".photo_url",
    "RowVersion": ".row_version",
    "Schedule": ".schedule",
    "ScheduleWorkPattern": ".schedule_work_pattern",
    "ScheduleWorkPatternEvenWeeks": ".schedule_work_pattern_even_weeks",
    "ScheduleWorkPatternOddWeeks": ".schedule_work_pattern_odd_weeks",
    "SortDirection": ".sort_direction",
    "Tax": ".tax",
    "TimeOffRequest": ".time_off_request",
    "TimeOffRequestNotes": ".time_off_request_notes",
    "TimeOffRequestRequestType": ".time_off_request_request_type",
    "TimeOffRequestStatus": ".time_off_request_status",
    "TimeOffRequestUnits": ".time_off_request_units",
    "TimeOffRequestsFilter": ".time_off_requests_filter",
    "TimeOffRequestsFilterTimeOffRequestStatus": ".time_off_requests_filter_time_off_request_status",
    "Title": ".title",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateDepartmentResponse": ".update_department_response",
    "UpdateEmployeeResponse": ".update_employee_response",
    "UpdateHrisCompanyResponse": ".update_hris_company_response",
    "UpdateTimeOffRequestResponse": ".update_time_off_request_response",
    "UpdatedAt": ".updated_at",
    "UpdatedBy": ".updated_by",
    "WebhookEvent": ".webhook_event",
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
    "Address",
    "AddressType",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "Benefit",
    "CompanyId",
    "CompanyName",
    "Compensation",
    "CreateDepartmentResponse",
    "CreateEmployeeResponse",
    "CreateHrisCompanyResponse",
    "CreateTimeOffRequestResponse",
    "CreatedAt",
    "CreatedBy",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "Deduction",
    "DeleteDepartmentResponse",
    "DeleteEmployeeResponse",
    "DeleteHrisCompanyResponse",
    "DeleteTimeOffRequestResponse",
    "Department",
    "Description",
    "Division",
    "Email",
    "EmailType",
    "Employee",
    "EmployeeCompensationsItem",
    "EmployeeCompensationsItemFlsaStatus",
    "EmployeeEmploymentRole",
    "EmployeeEmploymentRoleSubType",
    "EmployeeEmploymentRoleType",
    "EmployeeJobsItem",
    "EmployeeLeavingReason",
    "EmployeeManager",
    "EmployeeNumber",
    "EmployeePartner",
    "EmployeePayroll",
    "EmployeePayrolls",
    "EmployeeSchedules",
    "EmployeeSocialLinksItem",
    "EmployeeTeam",
    "EmployeesFilter",
    "EmployeesFilterEmploymentStatus",
    "EmployeesSort",
    "EmployeesSortBy",
    "EmploymentStatus",
    "FirstName",
    "Gender",
    "GetDepartmentResponse",
    "GetDepartmentsResponse",
    "GetEmployeePayrollResponse",
    "GetEmployeePayrollsResponse",
    "GetEmployeeResponse",
    "GetEmployeeSchedulesResponse",
    "GetEmployeesResponse",
    "GetHrisCompaniesResponse",
    "GetHrisCompanyResponse",
    "GetHrisJobResponse",
    "GetHrisJobsResponse",
    "GetPayrollResponse",
    "GetPayrollsResponse",
    "GetTimeOffRequestResponse",
    "GetTimeOffRequestsResponse",
    "HrisCompany",
    "HrisCompanyStatus",
    "HrisEventType",
    "HrisJob",
    "HrisJobLocation",
    "HrisJobs",
    "Id",
    "Language",
    "LastName",
    "Links",
    "Meta",
    "MetaCursors",
    "MiddleName",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PaymentRequiredResponse",
    "PaymentUnit",
    "Payroll",
    "PayrollTotals",
    "PayrollsFilter",
    "PhoneNumber",
    "PhoneNumberType",
    "PhotoUrl",
    "RowVersion",
    "Schedule",
    "ScheduleWorkPattern",
    "ScheduleWorkPatternEvenWeeks",
    "ScheduleWorkPatternOddWeeks",
    "SortDirection",
    "Tax",
    "TimeOffRequest",
    "TimeOffRequestNotes",
    "TimeOffRequestRequestType",
    "TimeOffRequestStatus",
    "TimeOffRequestUnits",
    "TimeOffRequestsFilter",
    "TimeOffRequestsFilterTimeOffRequestStatus",
    "Title",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateDepartmentResponse",
    "UpdateEmployeeResponse",
    "UpdateHrisCompanyResponse",
    "UpdateTimeOffRequestResponse",
    "UpdatedAt",
    "UpdatedBy",
    "WebhookEvent",
    "Website",
    "WebsiteType",
]
