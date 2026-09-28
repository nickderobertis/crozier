

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTransitionTrackerV3RequestSortBy(enum.StrEnum):
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
    DOB_ASC = "dob_asc"
    DOB_DESC = "dob_desc"
    ADMISSION_DATE_ASC = "admission_date_asc"
    ADMISSION_DATE_DESC = "admission_date_desc"
    TRANSITION_DATE_ASC = "transition_date_asc"
    TRANSITION_DATE_DESC = "transition_date_desc"
    TRANSITION_ROOM_ASC = "transition_room_asc"
    TRANSITION_ROOM_DESC = "transition_room_desc"
    DAYS_TO_TRANSITION_DATE_ASC = "days_to_transition_date_asc"
    DAYS_TO_TRANSITION_DATE_DESC = "days_to_transition_date_desc"
    WITHDRAWAL_DATE_ASC = "withdrawal_date_asc"
    WITHDRAWAL_DATE_DESC = "withdrawal_date_desc"

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
        dob_asc: typing.Callable[[], T_Result],
        dob_desc: typing.Callable[[], T_Result],
        admission_date_asc: typing.Callable[[], T_Result],
        admission_date_desc: typing.Callable[[], T_Result],
        transition_date_asc: typing.Callable[[], T_Result],
        transition_date_desc: typing.Callable[[], T_Result],
        transition_room_asc: typing.Callable[[], T_Result],
        transition_room_desc: typing.Callable[[], T_Result],
        days_to_transition_date_asc: typing.Callable[[], T_Result],
        days_to_transition_date_desc: typing.Callable[[], T_Result],
        withdrawal_date_asc: typing.Callable[[], T_Result],
        withdrawal_date_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTransitionTrackerV3RequestSortBy.NAME_ASC:
            return name_asc()
        if self is GetTransitionTrackerV3RequestSortBy.NAME_DESC:
            return name_desc()
        if self is GetTransitionTrackerV3RequestSortBy.SCHOOL_NAME_ASC:
            return school_name_asc()
        if self is GetTransitionTrackerV3RequestSortBy.SCHOOL_NAME_DESC:
            return school_name_desc()
        if self is GetTransitionTrackerV3RequestSortBy.STATUS_ASC:
            return status_asc()
        if self is GetTransitionTrackerV3RequestSortBy.STATUS_DESC:
            return status_desc()
        if self is GetTransitionTrackerV3RequestSortBy.ONBOARDING_STATUS_ASC:
            return onboarding_status_asc()
        if self is GetTransitionTrackerV3RequestSortBy.ONBOARDING_STATUS_DESC:
            return onboarding_status_desc()
        if self is GetTransitionTrackerV3RequestSortBy.ROOM_ASC:
            return room_asc()
        if self is GetTransitionTrackerV3RequestSortBy.ROOM_DESC:
            return room_desc()
        if self is GetTransitionTrackerV3RequestSortBy.ROOM_PROGRAM_ASC:
            return room_program_asc()
        if self is GetTransitionTrackerV3RequestSortBy.ROOM_PROGRAM_DESC:
            return room_program_desc()
        if self is GetTransitionTrackerV3RequestSortBy.DOB_ASC:
            return dob_asc()
        if self is GetTransitionTrackerV3RequestSortBy.DOB_DESC:
            return dob_desc()
        if self is GetTransitionTrackerV3RequestSortBy.ADMISSION_DATE_ASC:
            return admission_date_asc()
        if self is GetTransitionTrackerV3RequestSortBy.ADMISSION_DATE_DESC:
            return admission_date_desc()
        if self is GetTransitionTrackerV3RequestSortBy.TRANSITION_DATE_ASC:
            return transition_date_asc()
        if self is GetTransitionTrackerV3RequestSortBy.TRANSITION_DATE_DESC:
            return transition_date_desc()
        if self is GetTransitionTrackerV3RequestSortBy.TRANSITION_ROOM_ASC:
            return transition_room_asc()
        if self is GetTransitionTrackerV3RequestSortBy.TRANSITION_ROOM_DESC:
            return transition_room_desc()
        if self is GetTransitionTrackerV3RequestSortBy.DAYS_TO_TRANSITION_DATE_ASC:
            return days_to_transition_date_asc()
        if self is GetTransitionTrackerV3RequestSortBy.DAYS_TO_TRANSITION_DATE_DESC:
            return days_to_transition_date_desc()
        if self is GetTransitionTrackerV3RequestSortBy.WITHDRAWAL_DATE_ASC:
            return withdrawal_date_asc()
        if self is GetTransitionTrackerV3RequestSortBy.WITHDRAWAL_DATE_DESC:
            return withdrawal_date_desc()
