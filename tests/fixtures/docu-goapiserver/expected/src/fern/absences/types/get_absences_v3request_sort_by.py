

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAbsencesV3RequestSortBy(enum.StrEnum):
    DATE_ASC = "date_asc"
    DATE_DESC = "date_desc"
    STUDENT_ID_ASC = "student_id_asc"
    STUDENT_ID_DESC = "student_id_desc"

    def visit(
        self,
        date_asc: typing.Callable[[], T_Result],
        date_desc: typing.Callable[[], T_Result],
        student_id_asc: typing.Callable[[], T_Result],
        student_id_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAbsencesV3RequestSortBy.DATE_ASC:
            return date_asc()
        if self is GetAbsencesV3RequestSortBy.DATE_DESC:
            return date_desc()
        if self is GetAbsencesV3RequestSortBy.STUDENT_ID_ASC:
            return student_id_asc()
        if self is GetAbsencesV3RequestSortBy.STUDENT_ID_DESC:
            return student_id_desc()
