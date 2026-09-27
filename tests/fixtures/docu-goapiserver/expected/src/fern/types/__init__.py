



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .absence import Absence
    from .activity_summary_kid import ActivitySummaryKid
    from .activity_totals import ActivityTotals
    from .address import Address
    from .alert import Alert
    from .attendance import Attendance
    from .attendance_aggregate import AttendanceAggregate
    from .attendance_aggregate_group import AttendanceAggregateGroup
    from .attendance_aggregate_metrics import AttendanceAggregateMetrics
    from .available_space import AvailableSpace
    from .billing_attendance_audit import BillingAttendanceAudit
    from .billing_plan import BillingPlan
    from .billing_plan_aggregate import BillingPlanAggregate
    from .billing_plan_aggregate_group import BillingPlanAggregateGroup
    from .billing_plan_aggregate_metrics import BillingPlanAggregateMetrics
    from .bulk_lead_stages_item import BulkLeadStagesItem
    from .classroom_attendance import ClassroomAttendance
    from .closed_space_cell import ClosedSpaceCell
    from .company import Company
    from .company_settings import CompanySettings
    from .daily_activity import DailyActivity
    from .data_refresh import DataRefresh
    from .efficiency_ratio import EfficiencyRatio
    from .employee_time_off import EmployeeTimeOff
    from .enrollment_analytics import EnrollmentAnalytics
    from .enrollment_monthly import EnrollmentMonthly
    from .enrollment_period_analytics import EnrollmentPeriodAnalytics
    from .enrollment_tracker import EnrollmentTracker
    from .enrollment_trend import EnrollmentTrend
    from .error import Error
    from .fallout_metric import FalloutMetric
    from .fallout_year_summary import FalloutYearSummary
    from .family_balance import FamilyBalance
    from .family_balance_aggregate import FamilyBalanceAggregate
    from .family_balance_aggregate_group import FamilyBalanceAggregateGroup
    from .family_balance_aggregate_metrics import FamilyBalanceAggregateMetrics
    from .family_ledger import FamilyLedger
    from .family_transaction import FamilyTransaction
    from .gusto_company import GustoCompany
    from .gusto_contractor import GustoContractor
    from .gusto_employee import GustoEmployee
    from .intended_start_date_not_updated_lead import IntendedStartDateNotUpdatedLead
    from .intended_start_date_update import IntendedStartDateUpdate
    from .intended_start_date_update_intended_start_date import IntendedStartDateUpdateIntendedStartDate
    from .intended_start_date_update_intended_start_date_zero import IntendedStartDateUpdateIntendedStartDateZero
    from .intended_start_date_updated_lead import IntendedStartDateUpdatedLead
    from .lead import Lead
    from .lead_projection import LeadProjection
    from .lead_stage import LeadStage
    from .lead_stages import LeadStages
    from .new_start_student import NewStartStudent
    from .payment import Payment
    from .payment_aggregate import PaymentAggregate
    from .payment_aggregate_group import PaymentAggregateGroup
    from .payment_aggregate_metrics import PaymentAggregateMetrics
    from .payroll import Payroll
    from .payroll_data import PayrollData
    from .payroll_earnings import PayrollEarnings
    from .payroll_employee import PayrollEmployee
    from .payroll_item import PayrollItem
    from .payroll_period import PayrollPeriod
    from .payroll_total import PayrollTotal
    from .pre_registration_fallout_report import PreRegistrationFalloutReport
    from .pre_registration_fallout_student import PreRegistrationFalloutStudent
    from .procare_attendance_classroom import ProcareAttendanceClassroom
    from .procare_attendance_student import ProcareAttendanceStudent
    from .procare_message_created import ProcareMessageCreated
    from .procare_message_status import ProcareMessageStatus
    from .procare_message_task import ProcareMessageTask
    from .procare_staff import ProcareStaff
    from .ratio import Ratio
    from .room import Room
    from .school import School
    from .school_fallout_summary import SchoolFalloutSummary
    from .school_refresh import SchoolRefresh
    from .school_refresh_process import SchoolRefreshProcess
    from .session import Session
    from .sibling_discount import SiblingDiscount
    from .space_snapshot import SpaceSnapshot
    from .spaces_aggregate import SpacesAggregate
    from .spaces_periods import SpacesPeriods
    from .spaces_projection import SpacesProjection
    from .spaces_row import SpacesRow
    from .spaces_snapshot import SpacesSnapshot
    from .student import Student
    from .student_data import StudentData
    from .student_projection import StudentProjection
    from .tracker_period import TrackerPeriod
    from .tracker_room import TrackerRoom
    from .tracker_space import TrackerSpace
    from .tracker_student import TrackerStudent
    from .transition_student import TransitionStudent
    from .update_closed_spaces_response import UpdateClosedSpacesResponse
    from .update_intended_start_dates_response import UpdateIntendedStartDatesResponse
    from .update_lead_stages_request import UpdateLeadStagesRequest
    from .update_lead_stages_request_stage_inquiry_call_completed import (
        UpdateLeadStagesRequestStageInquiryCallCompleted,
    )
    from .update_lead_stages_request_stage_no_response import UpdateLeadStagesRequestStageNoResponse
    from .update_lead_stages_request_stage_no_response_timed_out import UpdateLeadStagesRequestStageNoResponseTimedOut
    from .update_lead_stages_request_stage_not_interested import UpdateLeadStagesRequestStageNotInterested
    from .update_lead_stages_request_stage_not_viable import UpdateLeadStagesRequestStageNotViable
    from .update_lead_stages_request_stage_tour_completed import UpdateLeadStagesRequestStageTourCompleted
    from .update_student_request import UpdateStudentRequest
    from .update_student_request_start_date_ems_entry import UpdateStudentRequestStartDateEmsEntry
    from .update_student_request_start_date_ems_entry_one import UpdateStudentRequestStartDateEmsEntryOne
    from .update_student_request_transition_date import UpdateStudentRequestTransitionDate
    from .update_student_request_transition_date2 import UpdateStudentRequestTransitionDate2
    from .update_student_request_transition_date2one import UpdateStudentRequestTransitionDate2One
    from .update_student_request_transition_date_one import UpdateStudentRequestTransitionDateOne
    from .update_student_request_transition_room2id import UpdateStudentRequestTransitionRoom2Id
    from .update_student_request_transition_room2id_one import UpdateStudentRequestTransitionRoom2IdOne
    from .update_student_request_transition_room_override_id import UpdateStudentRequestTransitionRoomOverrideId
    from .update_student_request_transition_room_override_id_one import UpdateStudentRequestTransitionRoomOverrideIdOne
    from .update_student_request_withdrawal_date_ems_entry import UpdateStudentRequestWithdrawalDateEmsEntry
    from .update_student_request_withdrawal_date_ems_entry_one import UpdateStudentRequestWithdrawalDateEmsEntryOne
    from .update_student_request_withdrawal_date_estimated import UpdateStudentRequestWithdrawalDateEstimated
    from .update_student_request_withdrawal_date_estimated_one import UpdateStudentRequestWithdrawalDateEstimatedOne
    from .update_student_response import UpdateStudentResponse
    from .user import User
    from .waitlist import Waitlist
    from .waitlist_room_eligibility import WaitlistRoomEligibility
    from .withdrawal_student import WithdrawalStudent
_dynamic_imports: typing.Dict[str, str] = {
    "Absence": ".absence",
    "ActivitySummaryKid": ".activity_summary_kid",
    "ActivityTotals": ".activity_totals",
    "Address": ".address",
    "Alert": ".alert",
    "Attendance": ".attendance",
    "AttendanceAggregate": ".attendance_aggregate",
    "AttendanceAggregateGroup": ".attendance_aggregate_group",
    "AttendanceAggregateMetrics": ".attendance_aggregate_metrics",
    "AvailableSpace": ".available_space",
    "BillingAttendanceAudit": ".billing_attendance_audit",
    "BillingPlan": ".billing_plan",
    "BillingPlanAggregate": ".billing_plan_aggregate",
    "BillingPlanAggregateGroup": ".billing_plan_aggregate_group",
    "BillingPlanAggregateMetrics": ".billing_plan_aggregate_metrics",
    "BulkLeadStagesItem": ".bulk_lead_stages_item",
    "ClassroomAttendance": ".classroom_attendance",
    "ClosedSpaceCell": ".closed_space_cell",
    "Company": ".company",
    "CompanySettings": ".company_settings",
    "DailyActivity": ".daily_activity",
    "DataRefresh": ".data_refresh",
    "EfficiencyRatio": ".efficiency_ratio",
    "EmployeeTimeOff": ".employee_time_off",
    "EnrollmentAnalytics": ".enrollment_analytics",
    "EnrollmentMonthly": ".enrollment_monthly",
    "EnrollmentPeriodAnalytics": ".enrollment_period_analytics",
    "EnrollmentTracker": ".enrollment_tracker",
    "EnrollmentTrend": ".enrollment_trend",
    "Error": ".error",
    "FalloutMetric": ".fallout_metric",
    "FalloutYearSummary": ".fallout_year_summary",
    "FamilyBalance": ".family_balance",
    "FamilyBalanceAggregate": ".family_balance_aggregate",
    "FamilyBalanceAggregateGroup": ".family_balance_aggregate_group",
    "FamilyBalanceAggregateMetrics": ".family_balance_aggregate_metrics",
    "FamilyLedger": ".family_ledger",
    "FamilyTransaction": ".family_transaction",
    "GustoCompany": ".gusto_company",
    "GustoContractor": ".gusto_contractor",
    "GustoEmployee": ".gusto_employee",
    "IntendedStartDateNotUpdatedLead": ".intended_start_date_not_updated_lead",
    "IntendedStartDateUpdate": ".intended_start_date_update",
    "IntendedStartDateUpdateIntendedStartDate": ".intended_start_date_update_intended_start_date",
    "IntendedStartDateUpdateIntendedStartDateZero": ".intended_start_date_update_intended_start_date_zero",
    "IntendedStartDateUpdatedLead": ".intended_start_date_updated_lead",
    "Lead": ".lead",
    "LeadProjection": ".lead_projection",
    "LeadStage": ".lead_stage",
    "LeadStages": ".lead_stages",
    "NewStartStudent": ".new_start_student",
    "Payment": ".payment",
    "PaymentAggregate": ".payment_aggregate",
    "PaymentAggregateGroup": ".payment_aggregate_group",
    "PaymentAggregateMetrics": ".payment_aggregate_metrics",
    "Payroll": ".payroll",
    "PayrollData": ".payroll_data",
    "PayrollEarnings": ".payroll_earnings",
    "PayrollEmployee": ".payroll_employee",
    "PayrollItem": ".payroll_item",
    "PayrollPeriod": ".payroll_period",
    "PayrollTotal": ".payroll_total",
    "PreRegistrationFalloutReport": ".pre_registration_fallout_report",
    "PreRegistrationFalloutStudent": ".pre_registration_fallout_student",
    "ProcareAttendanceClassroom": ".procare_attendance_classroom",
    "ProcareAttendanceStudent": ".procare_attendance_student",
    "ProcareMessageCreated": ".procare_message_created",
    "ProcareMessageStatus": ".procare_message_status",
    "ProcareMessageTask": ".procare_message_task",
    "ProcareStaff": ".procare_staff",
    "Ratio": ".ratio",
    "Room": ".room",
    "School": ".school",
    "SchoolFalloutSummary": ".school_fallout_summary",
    "SchoolRefresh": ".school_refresh",
    "SchoolRefreshProcess": ".school_refresh_process",
    "Session": ".session",
    "SiblingDiscount": ".sibling_discount",
    "SpaceSnapshot": ".space_snapshot",
    "SpacesAggregate": ".spaces_aggregate",
    "SpacesPeriods": ".spaces_periods",
    "SpacesProjection": ".spaces_projection",
    "SpacesRow": ".spaces_row",
    "SpacesSnapshot": ".spaces_snapshot",
    "Student": ".student",
    "StudentData": ".student_data",
    "StudentProjection": ".student_projection",
    "TrackerPeriod": ".tracker_period",
    "TrackerRoom": ".tracker_room",
    "TrackerSpace": ".tracker_space",
    "TrackerStudent": ".tracker_student",
    "TransitionStudent": ".transition_student",
    "UpdateClosedSpacesResponse": ".update_closed_spaces_response",
    "UpdateIntendedStartDatesResponse": ".update_intended_start_dates_response",
    "UpdateLeadStagesRequest": ".update_lead_stages_request",
    "UpdateLeadStagesRequestStageInquiryCallCompleted": ".update_lead_stages_request_stage_inquiry_call_completed",
    "UpdateLeadStagesRequestStageNoResponse": ".update_lead_stages_request_stage_no_response",
    "UpdateLeadStagesRequestStageNoResponseTimedOut": ".update_lead_stages_request_stage_no_response_timed_out",
    "UpdateLeadStagesRequestStageNotInterested": ".update_lead_stages_request_stage_not_interested",
    "UpdateLeadStagesRequestStageNotViable": ".update_lead_stages_request_stage_not_viable",
    "UpdateLeadStagesRequestStageTourCompleted": ".update_lead_stages_request_stage_tour_completed",
    "UpdateStudentRequest": ".update_student_request",
    "UpdateStudentRequestStartDateEmsEntry": ".update_student_request_start_date_ems_entry",
    "UpdateStudentRequestStartDateEmsEntryOne": ".update_student_request_start_date_ems_entry_one",
    "UpdateStudentRequestTransitionDate": ".update_student_request_transition_date",
    "UpdateStudentRequestTransitionDate2": ".update_student_request_transition_date2",
    "UpdateStudentRequestTransitionDate2One": ".update_student_request_transition_date2one",
    "UpdateStudentRequestTransitionDateOne": ".update_student_request_transition_date_one",
    "UpdateStudentRequestTransitionRoom2Id": ".update_student_request_transition_room2id",
    "UpdateStudentRequestTransitionRoom2IdOne": ".update_student_request_transition_room2id_one",
    "UpdateStudentRequestTransitionRoomOverrideId": ".update_student_request_transition_room_override_id",
    "UpdateStudentRequestTransitionRoomOverrideIdOne": ".update_student_request_transition_room_override_id_one",
    "UpdateStudentRequestWithdrawalDateEmsEntry": ".update_student_request_withdrawal_date_ems_entry",
    "UpdateStudentRequestWithdrawalDateEmsEntryOne": ".update_student_request_withdrawal_date_ems_entry_one",
    "UpdateStudentRequestWithdrawalDateEstimated": ".update_student_request_withdrawal_date_estimated",
    "UpdateStudentRequestWithdrawalDateEstimatedOne": ".update_student_request_withdrawal_date_estimated_one",
    "UpdateStudentResponse": ".update_student_response",
    "User": ".user",
    "Waitlist": ".waitlist",
    "WaitlistRoomEligibility": ".waitlist_room_eligibility",
    "WithdrawalStudent": ".withdrawal_student",
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
    "Absence",
    "ActivitySummaryKid",
    "ActivityTotals",
    "Address",
    "Alert",
    "Attendance",
    "AttendanceAggregate",
    "AttendanceAggregateGroup",
    "AttendanceAggregateMetrics",
    "AvailableSpace",
    "BillingAttendanceAudit",
    "BillingPlan",
    "BillingPlanAggregate",
    "BillingPlanAggregateGroup",
    "BillingPlanAggregateMetrics",
    "BulkLeadStagesItem",
    "ClassroomAttendance",
    "ClosedSpaceCell",
    "Company",
    "CompanySettings",
    "DailyActivity",
    "DataRefresh",
    "EfficiencyRatio",
    "EmployeeTimeOff",
    "EnrollmentAnalytics",
    "EnrollmentMonthly",
    "EnrollmentPeriodAnalytics",
    "EnrollmentTracker",
    "EnrollmentTrend",
    "Error",
    "FalloutMetric",
    "FalloutYearSummary",
    "FamilyBalance",
    "FamilyBalanceAggregate",
    "FamilyBalanceAggregateGroup",
    "FamilyBalanceAggregateMetrics",
    "FamilyLedger",
    "FamilyTransaction",
    "GustoCompany",
    "GustoContractor",
    "GustoEmployee",
    "IntendedStartDateNotUpdatedLead",
    "IntendedStartDateUpdate",
    "IntendedStartDateUpdateIntendedStartDate",
    "IntendedStartDateUpdateIntendedStartDateZero",
    "IntendedStartDateUpdatedLead",
    "Lead",
    "LeadProjection",
    "LeadStage",
    "LeadStages",
    "NewStartStudent",
    "Payment",
    "PaymentAggregate",
    "PaymentAggregateGroup",
    "PaymentAggregateMetrics",
    "Payroll",
    "PayrollData",
    "PayrollEarnings",
    "PayrollEmployee",
    "PayrollItem",
    "PayrollPeriod",
    "PayrollTotal",
    "PreRegistrationFalloutReport",
    "PreRegistrationFalloutStudent",
    "ProcareAttendanceClassroom",
    "ProcareAttendanceStudent",
    "ProcareMessageCreated",
    "ProcareMessageStatus",
    "ProcareMessageTask",
    "ProcareStaff",
    "Ratio",
    "Room",
    "School",
    "SchoolFalloutSummary",
    "SchoolRefresh",
    "SchoolRefreshProcess",
    "Session",
    "SiblingDiscount",
    "SpaceSnapshot",
    "SpacesAggregate",
    "SpacesPeriods",
    "SpacesProjection",
    "SpacesRow",
    "SpacesSnapshot",
    "Student",
    "StudentData",
    "StudentProjection",
    "TrackerPeriod",
    "TrackerRoom",
    "TrackerSpace",
    "TrackerStudent",
    "TransitionStudent",
    "UpdateClosedSpacesResponse",
    "UpdateIntendedStartDatesResponse",
    "UpdateLeadStagesRequest",
    "UpdateLeadStagesRequestStageInquiryCallCompleted",
    "UpdateLeadStagesRequestStageNoResponse",
    "UpdateLeadStagesRequestStageNoResponseTimedOut",
    "UpdateLeadStagesRequestStageNotInterested",
    "UpdateLeadStagesRequestStageNotViable",
    "UpdateLeadStagesRequestStageTourCompleted",
    "UpdateStudentRequest",
    "UpdateStudentRequestStartDateEmsEntry",
    "UpdateStudentRequestStartDateEmsEntryOne",
    "UpdateStudentRequestTransitionDate",
    "UpdateStudentRequestTransitionDate2",
    "UpdateStudentRequestTransitionDate2One",
    "UpdateStudentRequestTransitionDateOne",
    "UpdateStudentRequestTransitionRoom2Id",
    "UpdateStudentRequestTransitionRoom2IdOne",
    "UpdateStudentRequestTransitionRoomOverrideId",
    "UpdateStudentRequestTransitionRoomOverrideIdOne",
    "UpdateStudentRequestWithdrawalDateEmsEntry",
    "UpdateStudentRequestWithdrawalDateEmsEntryOne",
    "UpdateStudentRequestWithdrawalDateEstimated",
    "UpdateStudentRequestWithdrawalDateEstimatedOne",
    "UpdateStudentResponse",
    "User",
    "Waitlist",
    "WaitlistRoomEligibility",
    "WithdrawalStudent",
]
