

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSiblingDiscountsV3RequestSortBy(enum.StrEnum):
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    SCHOOL_NAME_ASC = "school_name_asc"
    SCHOOL_NAME_DESC = "school_name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"
    ROOM_ASC = "room_asc"
    ROOM_DESC = "room_desc"
    DOB_ASC = "dob_asc"
    DOB_DESC = "dob_desc"
    START_DATE_ASC = "start_date_asc"
    START_DATE_DESC = "start_date_desc"
    SIBLINGS_ASC = "siblings_asc"
    SIBLINGS_DESC = "siblings_desc"
    FAMILY_NAME_AND_DOB_ASC = "family_name_and_dob_asc"
    FAMILY_NAME_AND_DOB_DESC = "family_name_and_dob_desc"
    TUITION_PLAN_ASC = "tuition_plan_asc"
    TUITION_PLAN_DESC = "tuition_plan_desc"
    BILLING_CYCLE_ASC = "billing_cycle_asc"
    BILLING_CYCLE_DESC = "billing_cycle_desc"
    PLAN_STATUS_ASC = "plan_status_asc"
    PLAN_STATUS_DESC = "plan_status_desc"

    def visit(
        self,
        name_asc: typing.Callable[[], T_Result],
        name_desc: typing.Callable[[], T_Result],
        school_name_asc: typing.Callable[[], T_Result],
        school_name_desc: typing.Callable[[], T_Result],
        status_asc: typing.Callable[[], T_Result],
        status_desc: typing.Callable[[], T_Result],
        room_asc: typing.Callable[[], T_Result],
        room_desc: typing.Callable[[], T_Result],
        dob_asc: typing.Callable[[], T_Result],
        dob_desc: typing.Callable[[], T_Result],
        start_date_asc: typing.Callable[[], T_Result],
        start_date_desc: typing.Callable[[], T_Result],
        siblings_asc: typing.Callable[[], T_Result],
        siblings_desc: typing.Callable[[], T_Result],
        family_name_and_dob_asc: typing.Callable[[], T_Result],
        family_name_and_dob_desc: typing.Callable[[], T_Result],
        tuition_plan_asc: typing.Callable[[], T_Result],
        tuition_plan_desc: typing.Callable[[], T_Result],
        billing_cycle_asc: typing.Callable[[], T_Result],
        billing_cycle_desc: typing.Callable[[], T_Result],
        plan_status_asc: typing.Callable[[], T_Result],
        plan_status_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSiblingDiscountsV3RequestSortBy.NAME_ASC:
            return name_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.NAME_DESC:
            return name_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.SCHOOL_NAME_ASC:
            return school_name_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.SCHOOL_NAME_DESC:
            return school_name_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.STATUS_ASC:
            return status_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.STATUS_DESC:
            return status_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.ROOM_ASC:
            return room_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.ROOM_DESC:
            return room_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.DOB_ASC:
            return dob_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.DOB_DESC:
            return dob_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.START_DATE_ASC:
            return start_date_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.START_DATE_DESC:
            return start_date_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.SIBLINGS_ASC:
            return siblings_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.SIBLINGS_DESC:
            return siblings_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.FAMILY_NAME_AND_DOB_ASC:
            return family_name_and_dob_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.FAMILY_NAME_AND_DOB_DESC:
            return family_name_and_dob_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.TUITION_PLAN_ASC:
            return tuition_plan_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.TUITION_PLAN_DESC:
            return tuition_plan_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.BILLING_CYCLE_ASC:
            return billing_cycle_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.BILLING_CYCLE_DESC:
            return billing_cycle_desc()
        if self is GetSiblingDiscountsV3RequestSortBy.PLAN_STATUS_ASC:
            return plan_status_asc()
        if self is GetSiblingDiscountsV3RequestSortBy.PLAN_STATUS_DESC:
            return plan_status_desc()
