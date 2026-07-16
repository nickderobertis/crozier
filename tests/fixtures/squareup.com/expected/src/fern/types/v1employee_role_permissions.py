

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class V1EmployeeRolePermissions(str, enum.Enum):
    """ """

    REGISTER_ACCESS_SALES_HISTORY = "REGISTER_ACCESS_SALES_HISTORY"
    REGISTER_APPLY_RESTRICTED_DISCOUNTS = "REGISTER_APPLY_RESTRICTED_DISCOUNTS"
    REGISTER_CHANGE_SETTINGS = "REGISTER_CHANGE_SETTINGS"
    REGISTER_EDIT_ITEM = "REGISTER_EDIT_ITEM"
    REGISTER_ISSUE_REFUNDS = "REGISTER_ISSUE_REFUNDS"
    REGISTER_OPEN_CASH_DRAWER_OUTSIDE_SALE = "REGISTER_OPEN_CASH_DRAWER_OUTSIDE_SALE"
    REGISTER_VIEW_SUMMARY_REPORTS = "REGISTER_VIEW_SUMMARY_REPORTS"

    def visit(
        self,
        register_access_sales_history: typing.Callable[[], T_Result],
        register_apply_restricted_discounts: typing.Callable[[], T_Result],
        register_change_settings: typing.Callable[[], T_Result],
        register_edit_item: typing.Callable[[], T_Result],
        register_issue_refunds: typing.Callable[[], T_Result],
        register_open_cash_drawer_outside_sale: typing.Callable[[], T_Result],
        register_view_summary_reports: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1EmployeeRolePermissions.REGISTER_ACCESS_SALES_HISTORY:
            return register_access_sales_history()
        if self is V1EmployeeRolePermissions.REGISTER_APPLY_RESTRICTED_DISCOUNTS:
            return register_apply_restricted_discounts()
        if self is V1EmployeeRolePermissions.REGISTER_CHANGE_SETTINGS:
            return register_change_settings()
        if self is V1EmployeeRolePermissions.REGISTER_EDIT_ITEM:
            return register_edit_item()
        if self is V1EmployeeRolePermissions.REGISTER_ISSUE_REFUNDS:
            return register_issue_refunds()
        if self is V1EmployeeRolePermissions.REGISTER_OPEN_CASH_DRAWER_OUTSIDE_SALE:
            return register_open_cash_drawer_outside_sale()
        if self is V1EmployeeRolePermissions.REGISTER_VIEW_SUMMARY_REPORTS:
            return register_view_summary_reports()
