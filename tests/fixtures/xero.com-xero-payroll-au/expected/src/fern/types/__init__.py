



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account import Account
    from .account_type import AccountType
    from .allowance_type import AllowanceType
    from .api_exception import ApiException
    from .bank_account import BankAccount
    from .calendar_type import CalendarType
    from .deduction_line import DeductionLine
    from .deduction_type import DeductionType
    from .deduction_type_calculation_type import DeductionTypeCalculationType
    from .deduction_type_deduction_category import DeductionTypeDeductionCategory
    from .earnings_line import EarningsLine
    from .earnings_rate import EarningsRate
    from .earnings_rate_calculation_type import EarningsRateCalculationType
    from .earnings_type import EarningsType
    from .employee import Employee
    from .employee_gender import EmployeeGender
    from .employee_status import EmployeeStatus
    from .employees import Employees
    from .employment_basis import EmploymentBasis
    from .employment_termination_payment_type import EmploymentTerminationPaymentType
    from .entitlement_final_pay_payout_type import EntitlementFinalPayPayoutType
    from .home_address import HomeAddress
    from .leave_accrual_line import LeaveAccrualLine
    from .leave_application import LeaveApplication
    from .leave_applications import LeaveApplications
    from .leave_balance import LeaveBalance
    from .leave_earnings_line import LeaveEarningsLine
    from .leave_line import LeaveLine
    from .leave_line_calculation_type import LeaveLineCalculationType
    from .leave_lines import LeaveLines
    from .leave_period import LeavePeriod
    from .leave_period_status import LeavePeriodStatus
    from .leave_type import LeaveType
    from .leave_type_contribution_type import LeaveTypeContributionType
    from .manual_tax_type import ManualTaxType
    from .oauth_scope import OauthScope
    from .opening_balances import OpeningBalances
    from .pay_item import PayItem
    from .pay_items import PayItems
    from .pay_run import PayRun
    from .pay_run_status import PayRunStatus
    from .pay_runs import PayRuns
    from .pay_template import PayTemplate
    from .payment_frequency_type import PaymentFrequencyType
    from .payroll_calendar import PayrollCalendar
    from .payroll_calendars import PayrollCalendars
    from .payslip import Payslip
    from .payslip_lines import PayslipLines
    from .payslip_object import PayslipObject
    from .payslip_summary import PayslipSummary
    from .payslips import Payslips
    from .rate_type import RateType
    from .reimbursement_line import ReimbursementLine
    from .reimbursement_lines import ReimbursementLines
    from .reimbursement_type import ReimbursementType
    from .residency_status import ResidencyStatus
    from .settings import Settings
    from .settings_object import SettingsObject
    from .settings_tracking_categories import SettingsTrackingCategories
    from .settings_tracking_categories_employee_groups import SettingsTrackingCategoriesEmployeeGroups
    from .settings_tracking_categories_timesheet_categories import SettingsTrackingCategoriesTimesheetCategories
    from .state import State
    from .super_fund import SuperFund
    from .super_fund_product import SuperFundProduct
    from .super_fund_products import SuperFundProducts
    from .super_fund_type import SuperFundType
    from .super_funds import SuperFunds
    from .super_line import SuperLine
    from .super_membership import SuperMembership
    from .superannuation_calculation_type import SuperannuationCalculationType
    from .superannuation_contribution_type import SuperannuationContributionType
    from .superannuation_line import SuperannuationLine
    from .tax_declaration import TaxDeclaration
    from .tax_line import TaxLine
    from .tfn_exemption_type import TfnExemptionType
    from .timesheet import Timesheet
    from .timesheet_line import TimesheetLine
    from .timesheet_lines import TimesheetLines
    from .timesheet_object import TimesheetObject
    from .timesheet_status import TimesheetStatus
    from .timesheets import Timesheets
    from .validation_error import ValidationError
_dynamic_imports: typing.Dict[str, str] = {
    "Account": ".account",
    "AccountType": ".account_type",
    "AllowanceType": ".allowance_type",
    "ApiException": ".api_exception",
    "BankAccount": ".bank_account",
    "CalendarType": ".calendar_type",
    "DeductionLine": ".deduction_line",
    "DeductionType": ".deduction_type",
    "DeductionTypeCalculationType": ".deduction_type_calculation_type",
    "DeductionTypeDeductionCategory": ".deduction_type_deduction_category",
    "EarningsLine": ".earnings_line",
    "EarningsRate": ".earnings_rate",
    "EarningsRateCalculationType": ".earnings_rate_calculation_type",
    "EarningsType": ".earnings_type",
    "Employee": ".employee",
    "EmployeeGender": ".employee_gender",
    "EmployeeStatus": ".employee_status",
    "Employees": ".employees",
    "EmploymentBasis": ".employment_basis",
    "EmploymentTerminationPaymentType": ".employment_termination_payment_type",
    "EntitlementFinalPayPayoutType": ".entitlement_final_pay_payout_type",
    "HomeAddress": ".home_address",
    "LeaveAccrualLine": ".leave_accrual_line",
    "LeaveApplication": ".leave_application",
    "LeaveApplications": ".leave_applications",
    "LeaveBalance": ".leave_balance",
    "LeaveEarningsLine": ".leave_earnings_line",
    "LeaveLine": ".leave_line",
    "LeaveLineCalculationType": ".leave_line_calculation_type",
    "LeaveLines": ".leave_lines",
    "LeavePeriod": ".leave_period",
    "LeavePeriodStatus": ".leave_period_status",
    "LeaveType": ".leave_type",
    "LeaveTypeContributionType": ".leave_type_contribution_type",
    "ManualTaxType": ".manual_tax_type",
    "OauthScope": ".oauth_scope",
    "OpeningBalances": ".opening_balances",
    "PayItem": ".pay_item",
    "PayItems": ".pay_items",
    "PayRun": ".pay_run",
    "PayRunStatus": ".pay_run_status",
    "PayRuns": ".pay_runs",
    "PayTemplate": ".pay_template",
    "PaymentFrequencyType": ".payment_frequency_type",
    "PayrollCalendar": ".payroll_calendar",
    "PayrollCalendars": ".payroll_calendars",
    "Payslip": ".payslip",
    "PayslipLines": ".payslip_lines",
    "PayslipObject": ".payslip_object",
    "PayslipSummary": ".payslip_summary",
    "Payslips": ".payslips",
    "RateType": ".rate_type",
    "ReimbursementLine": ".reimbursement_line",
    "ReimbursementLines": ".reimbursement_lines",
    "ReimbursementType": ".reimbursement_type",
    "ResidencyStatus": ".residency_status",
    "Settings": ".settings",
    "SettingsObject": ".settings_object",
    "SettingsTrackingCategories": ".settings_tracking_categories",
    "SettingsTrackingCategoriesEmployeeGroups": ".settings_tracking_categories_employee_groups",
    "SettingsTrackingCategoriesTimesheetCategories": ".settings_tracking_categories_timesheet_categories",
    "State": ".state",
    "SuperFund": ".super_fund",
    "SuperFundProduct": ".super_fund_product",
    "SuperFundProducts": ".super_fund_products",
    "SuperFundType": ".super_fund_type",
    "SuperFunds": ".super_funds",
    "SuperLine": ".super_line",
    "SuperMembership": ".super_membership",
    "SuperannuationCalculationType": ".superannuation_calculation_type",
    "SuperannuationContributionType": ".superannuation_contribution_type",
    "SuperannuationLine": ".superannuation_line",
    "TaxDeclaration": ".tax_declaration",
    "TaxLine": ".tax_line",
    "TfnExemptionType": ".tfn_exemption_type",
    "Timesheet": ".timesheet",
    "TimesheetLine": ".timesheet_line",
    "TimesheetLines": ".timesheet_lines",
    "TimesheetObject": ".timesheet_object",
    "TimesheetStatus": ".timesheet_status",
    "Timesheets": ".timesheets",
    "ValidationError": ".validation_error",
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
    "Account",
    "AccountType",
    "AllowanceType",
    "ApiException",
    "BankAccount",
    "CalendarType",
    "DeductionLine",
    "DeductionType",
    "DeductionTypeCalculationType",
    "DeductionTypeDeductionCategory",
    "EarningsLine",
    "EarningsRate",
    "EarningsRateCalculationType",
    "EarningsType",
    "Employee",
    "EmployeeGender",
    "EmployeeStatus",
    "Employees",
    "EmploymentBasis",
    "EmploymentTerminationPaymentType",
    "EntitlementFinalPayPayoutType",
    "HomeAddress",
    "LeaveAccrualLine",
    "LeaveApplication",
    "LeaveApplications",
    "LeaveBalance",
    "LeaveEarningsLine",
    "LeaveLine",
    "LeaveLineCalculationType",
    "LeaveLines",
    "LeavePeriod",
    "LeavePeriodStatus",
    "LeaveType",
    "LeaveTypeContributionType",
    "ManualTaxType",
    "OauthScope",
    "OpeningBalances",
    "PayItem",
    "PayItems",
    "PayRun",
    "PayRunStatus",
    "PayRuns",
    "PayTemplate",
    "PaymentFrequencyType",
    "PayrollCalendar",
    "PayrollCalendars",
    "Payslip",
    "PayslipLines",
    "PayslipObject",
    "PayslipSummary",
    "Payslips",
    "RateType",
    "ReimbursementLine",
    "ReimbursementLines",
    "ReimbursementType",
    "ResidencyStatus",
    "Settings",
    "SettingsObject",
    "SettingsTrackingCategories",
    "SettingsTrackingCategoriesEmployeeGroups",
    "SettingsTrackingCategoriesTimesheetCategories",
    "State",
    "SuperFund",
    "SuperFundProduct",
    "SuperFundProducts",
    "SuperFundType",
    "SuperFunds",
    "SuperLine",
    "SuperMembership",
    "SuperannuationCalculationType",
    "SuperannuationContributionType",
    "SuperannuationLine",
    "TaxDeclaration",
    "TaxLine",
    "TfnExemptionType",
    "Timesheet",
    "TimesheetLine",
    "TimesheetLines",
    "TimesheetObject",
    "TimesheetStatus",
    "Timesheets",
    "ValidationError",
]
