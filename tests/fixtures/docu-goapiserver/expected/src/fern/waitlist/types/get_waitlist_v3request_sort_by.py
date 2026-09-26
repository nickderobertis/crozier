

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWaitlistV3RequestSortBy(enum.StrEnum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    SCHOOL_NAME_ASC = "school_name_asc"
    SCHOOL_NAME_DESC = "school_name_desc"
    PREFERRED_START_DATE_ASC = "preferred_start_date_asc"
    PREFERRED_START_DATE_DESC = "preferred_start_date_desc"
    PREFERRED_START_DATE_LAST_UPDATE_ASC = "preferred_start_date_last_update_asc"
    PREFERRED_START_DATE_LAST_UPDATE_DESC = "preferred_start_date_last_update_desc"
    AGE_PREFERRED_START_DATE_ASC = "age_preferred_start_date_asc"
    AGE_PREFERRED_START_DATE_DESC = "age_preferred_start_date_desc"
    ADMISSION_DATE_ASC = "admission_date_asc"
    ADMISSION_DATE_DESC = "admission_date_desc"
    LEAD_CREATED_DATE_ASC = "lead_created_date_asc"
    LEAD_CREATED_DATE_DESC = "lead_created_date_desc"
    DOB_ASC = "dob_asc"
    DOB_DESC = "dob_desc"
    SIBLINGS_ASC = "siblings_asc"
    SIBLINGS_DESC = "siblings_desc"

    def visit(
        self,
        name_asc: typing.Callable[[], T_Result],
        name_desc: typing.Callable[[], T_Result],
        school_name_asc: typing.Callable[[], T_Result],
        school_name_desc: typing.Callable[[], T_Result],
        preferred_start_date_asc: typing.Callable[[], T_Result],
        preferred_start_date_desc: typing.Callable[[], T_Result],
        preferred_start_date_last_update_asc: typing.Callable[[], T_Result],
        preferred_start_date_last_update_desc: typing.Callable[[], T_Result],
        age_preferred_start_date_asc: typing.Callable[[], T_Result],
        age_preferred_start_date_desc: typing.Callable[[], T_Result],
        admission_date_asc: typing.Callable[[], T_Result],
        admission_date_desc: typing.Callable[[], T_Result],
        lead_created_date_asc: typing.Callable[[], T_Result],
        lead_created_date_desc: typing.Callable[[], T_Result],
        dob_asc: typing.Callable[[], T_Result],
        dob_desc: typing.Callable[[], T_Result],
        siblings_asc: typing.Callable[[], T_Result],
        siblings_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWaitlistV3RequestSortBy.NAME_ASC:
            return name_asc()
        if self is GetWaitlistV3RequestSortBy.NAME_DESC:
            return name_desc()
        if self is GetWaitlistV3RequestSortBy.SCHOOL_NAME_ASC:
            return school_name_asc()
        if self is GetWaitlistV3RequestSortBy.SCHOOL_NAME_DESC:
            return school_name_desc()
        if self is GetWaitlistV3RequestSortBy.PREFERRED_START_DATE_ASC:
            return preferred_start_date_asc()
        if self is GetWaitlistV3RequestSortBy.PREFERRED_START_DATE_DESC:
            return preferred_start_date_desc()
        if self is GetWaitlistV3RequestSortBy.PREFERRED_START_DATE_LAST_UPDATE_ASC:
            return preferred_start_date_last_update_asc()
        if self is GetWaitlistV3RequestSortBy.PREFERRED_START_DATE_LAST_UPDATE_DESC:
            return preferred_start_date_last_update_desc()
        if self is GetWaitlistV3RequestSortBy.AGE_PREFERRED_START_DATE_ASC:
            return age_preferred_start_date_asc()
        if self is GetWaitlistV3RequestSortBy.AGE_PREFERRED_START_DATE_DESC:
            return age_preferred_start_date_desc()
        if self is GetWaitlistV3RequestSortBy.ADMISSION_DATE_ASC:
            return admission_date_asc()
        if self is GetWaitlistV3RequestSortBy.ADMISSION_DATE_DESC:
            return admission_date_desc()
        if self is GetWaitlistV3RequestSortBy.LEAD_CREATED_DATE_ASC:
            return lead_created_date_asc()
        if self is GetWaitlistV3RequestSortBy.LEAD_CREATED_DATE_DESC:
            return lead_created_date_desc()
        if self is GetWaitlistV3RequestSortBy.DOB_ASC:
            return dob_asc()
        if self is GetWaitlistV3RequestSortBy.DOB_DESC:
            return dob_desc()
        if self is GetWaitlistV3RequestSortBy.SIBLINGS_ASC:
            return siblings_asc()
        if self is GetWaitlistV3RequestSortBy.SIBLINGS_DESC:
            return siblings_desc()
