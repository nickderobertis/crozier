

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetNewStartTrackerV3RequestSortBy(enum.StrEnum):
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
    ROOM_PROGRAM_ASC = "room_program_asc"
    ROOM_PROGRAM_DESC = "room_program_desc"
    START_DATE_ASC = "start_date_asc"
    START_DATE_DESC = "start_date_desc"
    DAYS_TO_START_DATE_ASC = "days_to_start_date_asc"
    DAYS_TO_START_DATE_DESC = "days_to_start_date_desc"
    BILLING_CYCLE_ASC = "billing_cycle_asc"
    BILLING_CYCLE_DESC = "billing_cycle_desc"
    SIBLINGS_ASC = "siblings_asc"
    SIBLINGS_DESC = "siblings_desc"
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
        room_program_asc: typing.Callable[[], T_Result],
        room_program_desc: typing.Callable[[], T_Result],
        start_date_asc: typing.Callable[[], T_Result],
        start_date_desc: typing.Callable[[], T_Result],
        days_to_start_date_asc: typing.Callable[[], T_Result],
        days_to_start_date_desc: typing.Callable[[], T_Result],
        billing_cycle_asc: typing.Callable[[], T_Result],
        billing_cycle_desc: typing.Callable[[], T_Result],
        siblings_asc: typing.Callable[[], T_Result],
        siblings_desc: typing.Callable[[], T_Result],
        invoice_alert_asc: typing.Callable[[], T_Result],
        invoice_alert_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetNewStartTrackerV3RequestSortBy.NAME_ASC:
            return name_asc()
        if self is GetNewStartTrackerV3RequestSortBy.NAME_DESC:
            return name_desc()
        if self is GetNewStartTrackerV3RequestSortBy.SCHOOL_NAME_ASC:
            return school_name_asc()
        if self is GetNewStartTrackerV3RequestSortBy.SCHOOL_NAME_DESC:
            return school_name_desc()
        if self is GetNewStartTrackerV3RequestSortBy.STATUS_ASC:
            return status_asc()
        if self is GetNewStartTrackerV3RequestSortBy.STATUS_DESC:
            return status_desc()
        if self is GetNewStartTrackerV3RequestSortBy.ONBOARDING_STATUS_ASC:
            return onboarding_status_asc()
        if self is GetNewStartTrackerV3RequestSortBy.ONBOARDING_STATUS_DESC:
            return onboarding_status_desc()
        if self is GetNewStartTrackerV3RequestSortBy.ROOM_ASC:
            return room_asc()
        if self is GetNewStartTrackerV3RequestSortBy.ROOM_DESC:
            return room_desc()
        if self is GetNewStartTrackerV3RequestSortBy.ROOM_PROGRAM_ASC:
            return room_program_asc()
        if self is GetNewStartTrackerV3RequestSortBy.ROOM_PROGRAM_DESC:
            return room_program_desc()
        if self is GetNewStartTrackerV3RequestSortBy.START_DATE_ASC:
            return start_date_asc()
        if self is GetNewStartTrackerV3RequestSortBy.START_DATE_DESC:
            return start_date_desc()
        if self is GetNewStartTrackerV3RequestSortBy.DAYS_TO_START_DATE_ASC:
            return days_to_start_date_asc()
        if self is GetNewStartTrackerV3RequestSortBy.DAYS_TO_START_DATE_DESC:
            return days_to_start_date_desc()
        if self is GetNewStartTrackerV3RequestSortBy.BILLING_CYCLE_ASC:
            return billing_cycle_asc()
        if self is GetNewStartTrackerV3RequestSortBy.BILLING_CYCLE_DESC:
            return billing_cycle_desc()
        if self is GetNewStartTrackerV3RequestSortBy.SIBLINGS_ASC:
            return siblings_asc()
        if self is GetNewStartTrackerV3RequestSortBy.SIBLINGS_DESC:
            return siblings_desc()
        if self is GetNewStartTrackerV3RequestSortBy.INVOICE_ALERT_ASC:
            return invoice_alert_asc()
        if self is GetNewStartTrackerV3RequestSortBy.INVOICE_ALERT_DESC:
            return invoice_alert_desc()
