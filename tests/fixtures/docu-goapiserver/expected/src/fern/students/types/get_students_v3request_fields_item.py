

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetStudentsV3RequestFieldsItem(enum.StrEnum):
    ID = "id"
    MONDAY_ITEM_ID = "monday_item_id"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    SCHOOL_ID = "school_id"
    SCHOOL_NAME = "school_name"
    BIRTH_DATE = "birth_date"
    ADMISSION_DATE = "admission_date"
    PROCARE_STUDENT_STATUS = "procare_student_status"
    EMS_STUDENT_STATUS = "ems_student_status"
    ROOM_NAME = "room_name"
    ROOM_ID = "room_id"
    IS_PROCARE_DESKTOP_CLASSROOM_SCHEDULE_ROOM = "is_procare_desktop_classroom_schedule_room"
    START_DATE = "start_date"
    START_DATE_EMS_ENTRY = "start_date_ems_entry"
    PROCARE_START_DATE = "procare_start_date"
    PREFERRED_START_DATE = "preferred_start_date"
    WITHDRAWAL_DATE = "withdrawal_date"
    WITHDRAWAL_DATE_EMS_ENTRY = "withdrawal_date_ems_entry"
    WITHDRAWAL_DATE_ESTIMATED = "withdrawal_date_estimated"
    PROCARE_WITHDRAWAL_DATE = "procare_withdrawal_date"
    TRANSITION_DATE = "transition_date"
    TRANSITION_ROOM = "transition_room"
    TRANSITION_ROOM_ID = "transition_room_id"
    TRANSITION_ROOM_OVERRIDE = "transition_room_override"
    TRANSITION_ROOM_OVERRIDE_ID = "transition_room_override_id"
    TRANSITION_DATE2 = "transition_date_2"
    TRANSITION_ROOM2 = "transition_room_2"
    TRANSITION_ROOM2ID = "transition_room_2_id"
    DAYS_IN_ROOM = "days_in_room"
    ROOM_CHANGED_AT = "room_changed_at"
    LAST_VALID_ROOM_CHANGED_AT = "last_valid_room_changed_at"
    OLD_ROOM = "old_room"
    BILLING_PLAN = "billing_plan"
    PART_TIME = "part_time"
    SIBLINGS = "siblings"
    STAFF_CHILD = "staff_child"
    EMS_START_DATE = "ems_start_date"
    EMS_WITHDRAWAL_DATE = "ems_withdrawal_date"
    LEAD_SOURCE = "lead_source"
    COLOR_HEX = "color_hex"
    SHORT_NAME = "short_name"
    FAMILY_BALANCE = "family_balance"
    PARENT1NAME = "parent_1_name"
    PARENT1EMAIL = "parent_1_email"
    PARENT1MOBILE_PHONE = "parent_1_mobile_phone"
    PARENT2NAME = "parent_2_name"
    PARENT2EMAIL = "parent_2_email"
    PARENT2MOBILE_PHONE = "parent_2_mobile_phone"
    FAMILY_ID = "family_id"
    LAST_DAY_ATTENDED = "last_day_attended"
    DAYS_SINCE_LAST_ATTENDANCE = "days_since_last_attendance"
    PROCARE_DESKTOP_STATUS_END_DATE = "procare_desktop_status_end_date"
    PROCARE_DESKTOP_ENROLLMENT_STATUS = "procare_desktop_enrollment_status"
    PROCARE_DESKTOP_STATUS_END_DATE_NEXT = "procare_desktop_status_end_date_next"
    PROCARE_DESKTOP_ENROLLMENT_STATUS_NEXT = "procare_desktop_enrollment_status_next"
    IS_CREATED_FROM_PROCARE_DESKTOP = "is_created_from_procare_desktop"
    ENROLLMENT_ID = "enrollment_id"
    DAYS_ENROLLED = "days_enrolled"
    MONTHS_ENROLLED = "months_enrolled"
    AGE_AT_START_DATE = "age_at_start_date"
    AGE_AT_WITHDRAWAL_DATE = "age_at_withdrawal_date"
    ENROLLMENT_ELIGIBILITY = "enrollment_eligibility"
    ELIGIBLE_MONTHS_CAPTURE = "eligible_months_capture"
    ELIGIBLE_MONTHS_LOST = "eligible_months_lost"
    WITHDRAWAL_TYPE = "withdrawal_type"
    TRANSITION_ALERT = "transition_alert"
    TRANSITION_ALERT1CLEAR = "transition_alert_1_clear"
    TRANSITION_ALERT2CLEAR = "transition_alert_2_clear"
    TRANSITION_DATA_UPDATED_BY = "transition_data_updated_by"
    TRANSITION_DATA_UPDATED_AT = "transition_data_updated_at"
    TRACKER_NEW_CLASS = "tracker_new_class"
    ADDRESS = "address"
    FIELD_LABELS = "field_labels"
    ALERTS = "alerts"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        monday_item_id: typing.Callable[[], T_Result],
        first_name: typing.Callable[[], T_Result],
        last_name: typing.Callable[[], T_Result],
        school_id: typing.Callable[[], T_Result],
        school_name: typing.Callable[[], T_Result],
        birth_date: typing.Callable[[], T_Result],
        admission_date: typing.Callable[[], T_Result],
        procare_student_status: typing.Callable[[], T_Result],
        ems_student_status: typing.Callable[[], T_Result],
        room_name: typing.Callable[[], T_Result],
        room_id: typing.Callable[[], T_Result],
        is_procare_desktop_classroom_schedule_room: typing.Callable[[], T_Result],
        start_date: typing.Callable[[], T_Result],
        start_date_ems_entry: typing.Callable[[], T_Result],
        procare_start_date: typing.Callable[[], T_Result],
        preferred_start_date: typing.Callable[[], T_Result],
        withdrawal_date: typing.Callable[[], T_Result],
        withdrawal_date_ems_entry: typing.Callable[[], T_Result],
        withdrawal_date_estimated: typing.Callable[[], T_Result],
        procare_withdrawal_date: typing.Callable[[], T_Result],
        transition_date: typing.Callable[[], T_Result],
        transition_room: typing.Callable[[], T_Result],
        transition_room_id: typing.Callable[[], T_Result],
        transition_room_override: typing.Callable[[], T_Result],
        transition_room_override_id: typing.Callable[[], T_Result],
        transition_date2: typing.Callable[[], T_Result],
        transition_room2: typing.Callable[[], T_Result],
        transition_room2id: typing.Callable[[], T_Result],
        days_in_room: typing.Callable[[], T_Result],
        room_changed_at: typing.Callable[[], T_Result],
        last_valid_room_changed_at: typing.Callable[[], T_Result],
        old_room: typing.Callable[[], T_Result],
        billing_plan: typing.Callable[[], T_Result],
        part_time: typing.Callable[[], T_Result],
        siblings: typing.Callable[[], T_Result],
        staff_child: typing.Callable[[], T_Result],
        ems_start_date: typing.Callable[[], T_Result],
        ems_withdrawal_date: typing.Callable[[], T_Result],
        lead_source: typing.Callable[[], T_Result],
        color_hex: typing.Callable[[], T_Result],
        short_name: typing.Callable[[], T_Result],
        family_balance: typing.Callable[[], T_Result],
        parent1name: typing.Callable[[], T_Result],
        parent1email: typing.Callable[[], T_Result],
        parent1mobile_phone: typing.Callable[[], T_Result],
        parent2name: typing.Callable[[], T_Result],
        parent2email: typing.Callable[[], T_Result],
        parent2mobile_phone: typing.Callable[[], T_Result],
        family_id: typing.Callable[[], T_Result],
        last_day_attended: typing.Callable[[], T_Result],
        days_since_last_attendance: typing.Callable[[], T_Result],
        procare_desktop_status_end_date: typing.Callable[[], T_Result],
        procare_desktop_enrollment_status: typing.Callable[[], T_Result],
        procare_desktop_status_end_date_next: typing.Callable[[], T_Result],
        procare_desktop_enrollment_status_next: typing.Callable[[], T_Result],
        is_created_from_procare_desktop: typing.Callable[[], T_Result],
        enrollment_id: typing.Callable[[], T_Result],
        days_enrolled: typing.Callable[[], T_Result],
        months_enrolled: typing.Callable[[], T_Result],
        age_at_start_date: typing.Callable[[], T_Result],
        age_at_withdrawal_date: typing.Callable[[], T_Result],
        enrollment_eligibility: typing.Callable[[], T_Result],
        eligible_months_capture: typing.Callable[[], T_Result],
        eligible_months_lost: typing.Callable[[], T_Result],
        withdrawal_type: typing.Callable[[], T_Result],
        transition_alert: typing.Callable[[], T_Result],
        transition_alert1clear: typing.Callable[[], T_Result],
        transition_alert2clear: typing.Callable[[], T_Result],
        transition_data_updated_by: typing.Callable[[], T_Result],
        transition_data_updated_at: typing.Callable[[], T_Result],
        tracker_new_class: typing.Callable[[], T_Result],
        address: typing.Callable[[], T_Result],
        field_labels: typing.Callable[[], T_Result],
        alerts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetStudentsV3RequestFieldsItem.ID:
            return id()
        if self is GetStudentsV3RequestFieldsItem.MONDAY_ITEM_ID:
            return monday_item_id()
        if self is GetStudentsV3RequestFieldsItem.FIRST_NAME:
            return first_name()
        if self is GetStudentsV3RequestFieldsItem.LAST_NAME:
            return last_name()
        if self is GetStudentsV3RequestFieldsItem.SCHOOL_ID:
            return school_id()
        if self is GetStudentsV3RequestFieldsItem.SCHOOL_NAME:
            return school_name()
        if self is GetStudentsV3RequestFieldsItem.BIRTH_DATE:
            return birth_date()
        if self is GetStudentsV3RequestFieldsItem.ADMISSION_DATE:
            return admission_date()
        if self is GetStudentsV3RequestFieldsItem.PROCARE_STUDENT_STATUS:
            return procare_student_status()
        if self is GetStudentsV3RequestFieldsItem.EMS_STUDENT_STATUS:
            return ems_student_status()
        if self is GetStudentsV3RequestFieldsItem.ROOM_NAME:
            return room_name()
        if self is GetStudentsV3RequestFieldsItem.ROOM_ID:
            return room_id()
        if self is GetStudentsV3RequestFieldsItem.IS_PROCARE_DESKTOP_CLASSROOM_SCHEDULE_ROOM:
            return is_procare_desktop_classroom_schedule_room()
        if self is GetStudentsV3RequestFieldsItem.START_DATE:
            return start_date()
        if self is GetStudentsV3RequestFieldsItem.START_DATE_EMS_ENTRY:
            return start_date_ems_entry()
        if self is GetStudentsV3RequestFieldsItem.PROCARE_START_DATE:
            return procare_start_date()
        if self is GetStudentsV3RequestFieldsItem.PREFERRED_START_DATE:
            return preferred_start_date()
        if self is GetStudentsV3RequestFieldsItem.WITHDRAWAL_DATE:
            return withdrawal_date()
        if self is GetStudentsV3RequestFieldsItem.WITHDRAWAL_DATE_EMS_ENTRY:
            return withdrawal_date_ems_entry()
        if self is GetStudentsV3RequestFieldsItem.WITHDRAWAL_DATE_ESTIMATED:
            return withdrawal_date_estimated()
        if self is GetStudentsV3RequestFieldsItem.PROCARE_WITHDRAWAL_DATE:
            return procare_withdrawal_date()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_DATE:
            return transition_date()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ROOM:
            return transition_room()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ROOM_ID:
            return transition_room_id()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ROOM_OVERRIDE:
            return transition_room_override()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ROOM_OVERRIDE_ID:
            return transition_room_override_id()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_DATE2:
            return transition_date2()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ROOM2:
            return transition_room2()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ROOM2ID:
            return transition_room2id()
        if self is GetStudentsV3RequestFieldsItem.DAYS_IN_ROOM:
            return days_in_room()
        if self is GetStudentsV3RequestFieldsItem.ROOM_CHANGED_AT:
            return room_changed_at()
        if self is GetStudentsV3RequestFieldsItem.LAST_VALID_ROOM_CHANGED_AT:
            return last_valid_room_changed_at()
        if self is GetStudentsV3RequestFieldsItem.OLD_ROOM:
            return old_room()
        if self is GetStudentsV3RequestFieldsItem.BILLING_PLAN:
            return billing_plan()
        if self is GetStudentsV3RequestFieldsItem.PART_TIME:
            return part_time()
        if self is GetStudentsV3RequestFieldsItem.SIBLINGS:
            return siblings()
        if self is GetStudentsV3RequestFieldsItem.STAFF_CHILD:
            return staff_child()
        if self is GetStudentsV3RequestFieldsItem.EMS_START_DATE:
            return ems_start_date()
        if self is GetStudentsV3RequestFieldsItem.EMS_WITHDRAWAL_DATE:
            return ems_withdrawal_date()
        if self is GetStudentsV3RequestFieldsItem.LEAD_SOURCE:
            return lead_source()
        if self is GetStudentsV3RequestFieldsItem.COLOR_HEX:
            return color_hex()
        if self is GetStudentsV3RequestFieldsItem.SHORT_NAME:
            return short_name()
        if self is GetStudentsV3RequestFieldsItem.FAMILY_BALANCE:
            return family_balance()
        if self is GetStudentsV3RequestFieldsItem.PARENT1NAME:
            return parent1name()
        if self is GetStudentsV3RequestFieldsItem.PARENT1EMAIL:
            return parent1email()
        if self is GetStudentsV3RequestFieldsItem.PARENT1MOBILE_PHONE:
            return parent1mobile_phone()
        if self is GetStudentsV3RequestFieldsItem.PARENT2NAME:
            return parent2name()
        if self is GetStudentsV3RequestFieldsItem.PARENT2EMAIL:
            return parent2email()
        if self is GetStudentsV3RequestFieldsItem.PARENT2MOBILE_PHONE:
            return parent2mobile_phone()
        if self is GetStudentsV3RequestFieldsItem.FAMILY_ID:
            return family_id()
        if self is GetStudentsV3RequestFieldsItem.LAST_DAY_ATTENDED:
            return last_day_attended()
        if self is GetStudentsV3RequestFieldsItem.DAYS_SINCE_LAST_ATTENDANCE:
            return days_since_last_attendance()
        if self is GetStudentsV3RequestFieldsItem.PROCARE_DESKTOP_STATUS_END_DATE:
            return procare_desktop_status_end_date()
        if self is GetStudentsV3RequestFieldsItem.PROCARE_DESKTOP_ENROLLMENT_STATUS:
            return procare_desktop_enrollment_status()
        if self is GetStudentsV3RequestFieldsItem.PROCARE_DESKTOP_STATUS_END_DATE_NEXT:
            return procare_desktop_status_end_date_next()
        if self is GetStudentsV3RequestFieldsItem.PROCARE_DESKTOP_ENROLLMENT_STATUS_NEXT:
            return procare_desktop_enrollment_status_next()
        if self is GetStudentsV3RequestFieldsItem.IS_CREATED_FROM_PROCARE_DESKTOP:
            return is_created_from_procare_desktop()
        if self is GetStudentsV3RequestFieldsItem.ENROLLMENT_ID:
            return enrollment_id()
        if self is GetStudentsV3RequestFieldsItem.DAYS_ENROLLED:
            return days_enrolled()
        if self is GetStudentsV3RequestFieldsItem.MONTHS_ENROLLED:
            return months_enrolled()
        if self is GetStudentsV3RequestFieldsItem.AGE_AT_START_DATE:
            return age_at_start_date()
        if self is GetStudentsV3RequestFieldsItem.AGE_AT_WITHDRAWAL_DATE:
            return age_at_withdrawal_date()
        if self is GetStudentsV3RequestFieldsItem.ENROLLMENT_ELIGIBILITY:
            return enrollment_eligibility()
        if self is GetStudentsV3RequestFieldsItem.ELIGIBLE_MONTHS_CAPTURE:
            return eligible_months_capture()
        if self is GetStudentsV3RequestFieldsItem.ELIGIBLE_MONTHS_LOST:
            return eligible_months_lost()
        if self is GetStudentsV3RequestFieldsItem.WITHDRAWAL_TYPE:
            return withdrawal_type()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ALERT:
            return transition_alert()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ALERT1CLEAR:
            return transition_alert1clear()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_ALERT2CLEAR:
            return transition_alert2clear()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_DATA_UPDATED_BY:
            return transition_data_updated_by()
        if self is GetStudentsV3RequestFieldsItem.TRANSITION_DATA_UPDATED_AT:
            return transition_data_updated_at()
        if self is GetStudentsV3RequestFieldsItem.TRACKER_NEW_CLASS:
            return tracker_new_class()
        if self is GetStudentsV3RequestFieldsItem.ADDRESS:
            return address()
        if self is GetStudentsV3RequestFieldsItem.FIELD_LABELS:
            return field_labels()
        if self is GetStudentsV3RequestFieldsItem.ALERTS:
            return alerts()
