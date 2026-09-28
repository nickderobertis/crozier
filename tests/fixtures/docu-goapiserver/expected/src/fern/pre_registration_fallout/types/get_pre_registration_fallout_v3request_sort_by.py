

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPreRegistrationFalloutV3RequestSortBy(enum.StrEnum):
    STUDENT_NAME_ASC = "student_name_asc"
    STUDENT_NAME_DESC = "student_name_desc"
    SCHOOL_NAME_ASC = "school_name_asc"
    SCHOOL_NAME_DESC = "school_name_desc"
    YEAR_ASC = "year_asc"
    YEAR_DESC = "year_desc"
    PRE_REGISTRATION_DATE_ASC = "pre_registration_date_asc"
    PRE_REGISTRATION_DATE_DESC = "pre_registration_date_desc"
    WITHDRAWAL_DATE_ASC = "withdrawal_date_asc"
    WITHDRAWAL_DATE_DESC = "withdrawal_date_desc"
    WITHDREW_SAME_YEAR_ASC = "withdrew_same_year_asc"
    WITHDREW_SAME_YEAR_DESC = "withdrew_same_year_desc"
    STUDENT_STATUS_ASC = "student_status_asc"
    STUDENT_STATUS_DESC = "student_status_desc"

    def visit(
        self,
        student_name_asc: typing.Callable[[], T_Result],
        student_name_desc: typing.Callable[[], T_Result],
        school_name_asc: typing.Callable[[], T_Result],
        school_name_desc: typing.Callable[[], T_Result],
        year_asc: typing.Callable[[], T_Result],
        year_desc: typing.Callable[[], T_Result],
        pre_registration_date_asc: typing.Callable[[], T_Result],
        pre_registration_date_desc: typing.Callable[[], T_Result],
        withdrawal_date_asc: typing.Callable[[], T_Result],
        withdrawal_date_desc: typing.Callable[[], T_Result],
        withdrew_same_year_asc: typing.Callable[[], T_Result],
        withdrew_same_year_desc: typing.Callable[[], T_Result],
        student_status_asc: typing.Callable[[], T_Result],
        student_status_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetPreRegistrationFalloutV3RequestSortBy.STUDENT_NAME_ASC:
            return student_name_asc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.STUDENT_NAME_DESC:
            return student_name_desc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.SCHOOL_NAME_ASC:
            return school_name_asc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.SCHOOL_NAME_DESC:
            return school_name_desc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.YEAR_ASC:
            return year_asc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.YEAR_DESC:
            return year_desc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.PRE_REGISTRATION_DATE_ASC:
            return pre_registration_date_asc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.PRE_REGISTRATION_DATE_DESC:
            return pre_registration_date_desc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.WITHDRAWAL_DATE_ASC:
            return withdrawal_date_asc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.WITHDRAWAL_DATE_DESC:
            return withdrawal_date_desc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.WITHDREW_SAME_YEAR_ASC:
            return withdrew_same_year_asc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.WITHDREW_SAME_YEAR_DESC:
            return withdrew_same_year_desc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.STUDENT_STATUS_ASC:
            return student_status_asc()
        if self is GetPreRegistrationFalloutV3RequestSortBy.STUDENT_STATUS_DESC:
            return student_status_desc()
