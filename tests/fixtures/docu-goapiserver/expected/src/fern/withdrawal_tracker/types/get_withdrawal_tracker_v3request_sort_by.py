

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWithdrawalTrackerV3RequestSortBy(enum.StrEnum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    SCHOOL_NAME_ASC = "school_name_asc"
    SCHOOL_NAME_DESC = "school_name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    ONBOARDING_STATUS_ASC = "onboarding_status_asc"
    ONBOARDING_STATUS_DESC = "onboarding_status_desc"
    ROOM_ASC = "room_asc"
    ROOM_DESC = "room_desc"
    START_DATE_ASC = "start_date_asc"
    START_DATE_DESC = "start_date_desc"
    WITHDRAWAL_DATE_ASC = "withdrawal_date_asc"
    WITHDRAWAL_DATE_DESC = "withdrawal_date_desc"
    WITHDRAWAL_DATE_ESTIMATED_ASC = "withdrawal_date_estimated_asc"
    WITHDRAWAL_DATE_ESTIMATED_DESC = "withdrawal_date_estimated_desc"
    WITHDRAWAL_TYPE_ASC = "withdrawal_type_asc"
    WITHDRAWAL_TYPE_DESC = "withdrawal_type_desc"
    DAYS_TO_WITHDRAWAL_DATE_ASC = "days_to_withdrawal_date_asc"
    DAYS_TO_WITHDRAWAL_DATE_DESC = "days_to_withdrawal_date_desc"
    PLAN_STATUS_ASC = "plan_status_asc"
    PLAN_STATUS_DESC = "plan_status_desc"
    BILLING_CYCLE_ASC = "billing_cycle_asc"
    BILLING_CYCLE_DESC = "billing_cycle_desc"
    PRO_RATE_FACTOR_WD_ASC = "pro_rate_factor_wd_asc"
    PRO_RATE_FACTOR_WD_DESC = "pro_rate_factor_wd_desc"
    INVOICE_ALERT_ASC = "invoice_alert_asc"
    INVOICE_ALERT_DESC = "invoice_alert_desc"

    def visit(
        self,
        name_asc: typing.Callable[[], T_Result],
        name_desc: typing.Callable[[], T_Result],
        school_name_asc: typing.Callable[[], T_Result],
        school_name_desc: typing.Callable[[], T_Result],
        status_asc: typing.Callable[[], T_Result],
        status_desc: typing.Callable[[], T_Result],
        onboarding_status_asc: typing.Callable[[], T_Result],
        onboarding_status_desc: typing.Callable[[], T_Result],
        room_asc: typing.Callable[[], T_Result],
        room_desc: typing.Callable[[], T_Result],
        start_date_asc: typing.Callable[[], T_Result],
        start_date_desc: typing.Callable[[], T_Result],
        withdrawal_date_asc: typing.Callable[[], T_Result],
        withdrawal_date_desc: typing.Callable[[], T_Result],
        withdrawal_date_estimated_asc: typing.Callable[[], T_Result],
        withdrawal_date_estimated_desc: typing.Callable[[], T_Result],
        withdrawal_type_asc: typing.Callable[[], T_Result],
        withdrawal_type_desc: typing.Callable[[], T_Result],
        days_to_withdrawal_date_asc: typing.Callable[[], T_Result],
        days_to_withdrawal_date_desc: typing.Callable[[], T_Result],
        plan_status_asc: typing.Callable[[], T_Result],
        plan_status_desc: typing.Callable[[], T_Result],
        billing_cycle_asc: typing.Callable[[], T_Result],
        billing_cycle_desc: typing.Callable[[], T_Result],
        pro_rate_factor_wd_asc: typing.Callable[[], T_Result],
        pro_rate_factor_wd_desc: typing.Callable[[], T_Result],
        invoice_alert_asc: typing.Callable[[], T_Result],
        invoice_alert_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWithdrawalTrackerV3RequestSortBy.NAME_ASC:
            return name_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.NAME_DESC:
            return name_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.SCHOOL_NAME_ASC:
            return school_name_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.SCHOOL_NAME_DESC:
            return school_name_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.STATUS_ASC:
            return status_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.STATUS_DESC:
            return status_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.ONBOARDING_STATUS_ASC:
            return onboarding_status_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.ONBOARDING_STATUS_DESC:
            return onboarding_status_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.ROOM_ASC:
            return room_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.ROOM_DESC:
            return room_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.START_DATE_ASC:
            return start_date_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.START_DATE_DESC:
            return start_date_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.WITHDRAWAL_DATE_ASC:
            return withdrawal_date_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.WITHDRAWAL_DATE_DESC:
            return withdrawal_date_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.WITHDRAWAL_DATE_ESTIMATED_ASC:
            return withdrawal_date_estimated_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.WITHDRAWAL_DATE_ESTIMATED_DESC:
            return withdrawal_date_estimated_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.WITHDRAWAL_TYPE_ASC:
            return withdrawal_type_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.WITHDRAWAL_TYPE_DESC:
            return withdrawal_type_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.DAYS_TO_WITHDRAWAL_DATE_ASC:
            return days_to_withdrawal_date_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.DAYS_TO_WITHDRAWAL_DATE_DESC:
            return days_to_withdrawal_date_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.PLAN_STATUS_ASC:
            return plan_status_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.PLAN_STATUS_DESC:
            return plan_status_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.BILLING_CYCLE_ASC:
            return billing_cycle_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.BILLING_CYCLE_DESC:
            return billing_cycle_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.PRO_RATE_FACTOR_WD_ASC:
            return pro_rate_factor_wd_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.PRO_RATE_FACTOR_WD_DESC:
            return pro_rate_factor_wd_desc()
        if self is GetWithdrawalTrackerV3RequestSortBy.INVOICE_ALERT_ASC:
            return invoice_alert_asc()
        if self is GetWithdrawalTrackerV3RequestSortBy.INVOICE_ALERT_DESC:
            return invoice_alert_desc()
