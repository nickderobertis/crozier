

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLeadsV3RequestFieldsItem(enum.StrEnum):
    LEAD_ID = "lead_id"
    MONDAY_ITEM_ID = "monday_item_id"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    SCHOOL_ID = "school_id"
    SCHOOL_NAME = "school_name"
    STATUS = "status"
    DATE_OF_BIRTH = "date_of_birth"
    CURRENT_AGE = "current_age"
    INTENDED_START_DATE = "intended_start_date"
    PERIODS_LEAD_ROOM_AVAILABLE = "periods_lead_room_available"
    PARENT1NAME = "parent1_name"
    PARENT1EMAIL = "parent1_email"
    PARENT1MOBILE = "parent1_mobile"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    AVAILABLE_SPACE = "available_space"
    SOURCE = "source"
    INTELLIKID_STATUS = "intellikid_status"
    INTELLIKID_CHILDREN_STATUS = "intellikid_children_status"
    INTELLIKID_LEAD_STATUS = "intellikid_lead_status"
    INTELLIKID_SOURCE = "intellikid_source"
    NOTES = "notes"
    STUDENT_STATUS = "student_status"
    ONBOARDING_STATUS = "onboarding_status"
    EMS_STATUS = "ems_status"
    START_DATE = "start_date"
    WITHDRAWAL_DATE = "withdrawal_date"
    LINELEADER_CHILD_ID = "lineleader_child_id"
    LINELEADER_FAMILY_ID = "lineleader_family_id"
    LINELEADER_CENTER_ID = "lineleader_center_id"
    LINELEADER_CENTER_NAME = "lineleader_center_name"
    LINELEADER_STATUS = "lineleader_status"
    LINELEADER_CLASSROOM = "lineleader_classroom"
    STAGE_INQUIRY_CALL_COMPLETED = "stage_inquiry_call_completed"
    STAGE_TOUR_COMPLETED = "stage_tour_completed"
    STAGE_NOT_VIABLE = "stage_not_viable"
    STAGE_NOT_INTERESTED = "stage_not_interested"
    STAGE_NO_RESPONSE = "stage_no_response"
    STAGE_NO_RESPONSE_TIMED_OUT = "stage_no_response_timed_out"
    IS_CRM_INTENDED_START_DATE = "is_crm_intended_start_date"
    LEAD_TO_ENROLLMENT_DATE = "lead_to_enrollment_date"
    AGE_AT_START_DATE_MONTHS = "age_at_start_date_months"
    AGE_AT_LEAD_CREATED_AT_MONTHS = "age_at_lead_created_at_months"
    ALERTS = "alerts"

    def visit(
        self,
        lead_id: typing.Callable[[], T_Result],
        monday_item_id: typing.Callable[[], T_Result],
        first_name: typing.Callable[[], T_Result],
        last_name: typing.Callable[[], T_Result],
        school_id: typing.Callable[[], T_Result],
        school_name: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        date_of_birth: typing.Callable[[], T_Result],
        current_age: typing.Callable[[], T_Result],
        intended_start_date: typing.Callable[[], T_Result],
        periods_lead_room_available: typing.Callable[[], T_Result],
        parent1name: typing.Callable[[], T_Result],
        parent1email: typing.Callable[[], T_Result],
        parent1mobile: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        available_space: typing.Callable[[], T_Result],
        source: typing.Callable[[], T_Result],
        intellikid_status: typing.Callable[[], T_Result],
        intellikid_children_status: typing.Callable[[], T_Result],
        intellikid_lead_status: typing.Callable[[], T_Result],
        intellikid_source: typing.Callable[[], T_Result],
        notes: typing.Callable[[], T_Result],
        student_status: typing.Callable[[], T_Result],
        onboarding_status: typing.Callable[[], T_Result],
        ems_status: typing.Callable[[], T_Result],
        start_date: typing.Callable[[], T_Result],
        withdrawal_date: typing.Callable[[], T_Result],
        lineleader_child_id: typing.Callable[[], T_Result],
        lineleader_family_id: typing.Callable[[], T_Result],
        lineleader_center_id: typing.Callable[[], T_Result],
        lineleader_center_name: typing.Callable[[], T_Result],
        lineleader_status: typing.Callable[[], T_Result],
        lineleader_classroom: typing.Callable[[], T_Result],
        stage_inquiry_call_completed: typing.Callable[[], T_Result],
        stage_tour_completed: typing.Callable[[], T_Result],
        stage_not_viable: typing.Callable[[], T_Result],
        stage_not_interested: typing.Callable[[], T_Result],
        stage_no_response: typing.Callable[[], T_Result],
        stage_no_response_timed_out: typing.Callable[[], T_Result],
        is_crm_intended_start_date: typing.Callable[[], T_Result],
        lead_to_enrollment_date: typing.Callable[[], T_Result],
        age_at_start_date_months: typing.Callable[[], T_Result],
        age_at_lead_created_at_months: typing.Callable[[], T_Result],
        alerts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetLeadsV3RequestFieldsItem.LEAD_ID:
            return lead_id()
        if self is GetLeadsV3RequestFieldsItem.MONDAY_ITEM_ID:
            return monday_item_id()
        if self is GetLeadsV3RequestFieldsItem.FIRST_NAME:
            return first_name()
        if self is GetLeadsV3RequestFieldsItem.LAST_NAME:
            return last_name()
        if self is GetLeadsV3RequestFieldsItem.SCHOOL_ID:
            return school_id()
        if self is GetLeadsV3RequestFieldsItem.SCHOOL_NAME:
            return school_name()
        if self is GetLeadsV3RequestFieldsItem.STATUS:
            return status()
        if self is GetLeadsV3RequestFieldsItem.DATE_OF_BIRTH:
            return date_of_birth()
        if self is GetLeadsV3RequestFieldsItem.CURRENT_AGE:
            return current_age()
        if self is GetLeadsV3RequestFieldsItem.INTENDED_START_DATE:
            return intended_start_date()
        if self is GetLeadsV3RequestFieldsItem.PERIODS_LEAD_ROOM_AVAILABLE:
            return periods_lead_room_available()
        if self is GetLeadsV3RequestFieldsItem.PARENT1NAME:
            return parent1name()
        if self is GetLeadsV3RequestFieldsItem.PARENT1EMAIL:
            return parent1email()
        if self is GetLeadsV3RequestFieldsItem.PARENT1MOBILE:
            return parent1mobile()
        if self is GetLeadsV3RequestFieldsItem.CREATED_AT:
            return created_at()
        if self is GetLeadsV3RequestFieldsItem.UPDATED_AT:
            return updated_at()
        if self is GetLeadsV3RequestFieldsItem.AVAILABLE_SPACE:
            return available_space()
        if self is GetLeadsV3RequestFieldsItem.SOURCE:
            return source()
        if self is GetLeadsV3RequestFieldsItem.INTELLIKID_STATUS:
            return intellikid_status()
        if self is GetLeadsV3RequestFieldsItem.INTELLIKID_CHILDREN_STATUS:
            return intellikid_children_status()
        if self is GetLeadsV3RequestFieldsItem.INTELLIKID_LEAD_STATUS:
            return intellikid_lead_status()
        if self is GetLeadsV3RequestFieldsItem.INTELLIKID_SOURCE:
            return intellikid_source()
        if self is GetLeadsV3RequestFieldsItem.NOTES:
            return notes()
        if self is GetLeadsV3RequestFieldsItem.STUDENT_STATUS:
            return student_status()
        if self is GetLeadsV3RequestFieldsItem.ONBOARDING_STATUS:
            return onboarding_status()
        if self is GetLeadsV3RequestFieldsItem.EMS_STATUS:
            return ems_status()
        if self is GetLeadsV3RequestFieldsItem.START_DATE:
            return start_date()
        if self is GetLeadsV3RequestFieldsItem.WITHDRAWAL_DATE:
            return withdrawal_date()
        if self is GetLeadsV3RequestFieldsItem.LINELEADER_CHILD_ID:
            return lineleader_child_id()
        if self is GetLeadsV3RequestFieldsItem.LINELEADER_FAMILY_ID:
            return lineleader_family_id()
        if self is GetLeadsV3RequestFieldsItem.LINELEADER_CENTER_ID:
            return lineleader_center_id()
        if self is GetLeadsV3RequestFieldsItem.LINELEADER_CENTER_NAME:
            return lineleader_center_name()
        if self is GetLeadsV3RequestFieldsItem.LINELEADER_STATUS:
            return lineleader_status()
        if self is GetLeadsV3RequestFieldsItem.LINELEADER_CLASSROOM:
            return lineleader_classroom()
        if self is GetLeadsV3RequestFieldsItem.STAGE_INQUIRY_CALL_COMPLETED:
            return stage_inquiry_call_completed()
        if self is GetLeadsV3RequestFieldsItem.STAGE_TOUR_COMPLETED:
            return stage_tour_completed()
        if self is GetLeadsV3RequestFieldsItem.STAGE_NOT_VIABLE:
            return stage_not_viable()
        if self is GetLeadsV3RequestFieldsItem.STAGE_NOT_INTERESTED:
            return stage_not_interested()
        if self is GetLeadsV3RequestFieldsItem.STAGE_NO_RESPONSE:
            return stage_no_response()
        if self is GetLeadsV3RequestFieldsItem.STAGE_NO_RESPONSE_TIMED_OUT:
            return stage_no_response_timed_out()
        if self is GetLeadsV3RequestFieldsItem.IS_CRM_INTENDED_START_DATE:
            return is_crm_intended_start_date()
        if self is GetLeadsV3RequestFieldsItem.LEAD_TO_ENROLLMENT_DATE:
            return lead_to_enrollment_date()
        if self is GetLeadsV3RequestFieldsItem.AGE_AT_START_DATE_MONTHS:
            return age_at_start_date_months()
        if self is GetLeadsV3RequestFieldsItem.AGE_AT_LEAD_CREATED_AT_MONTHS:
            return age_at_lead_created_at_months()
        if self is GetLeadsV3RequestFieldsItem.ALERTS:
            return alerts()
