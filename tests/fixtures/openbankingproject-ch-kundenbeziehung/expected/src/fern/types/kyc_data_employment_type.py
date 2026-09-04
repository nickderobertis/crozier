

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KycDataEmploymentType(enum.StrEnum):
    EMPLOYED = "employed"
    SELF_EMPLOYED = "self_employed"
    UNEMPLOYED = "unemployed"
    RETIRED = "retired"
    STUDENT = "student"

    def visit(
        self,
        employed: typing.Callable[[], T_Result],
        self_employed: typing.Callable[[], T_Result],
        unemployed: typing.Callable[[], T_Result],
        retired: typing.Callable[[], T_Result],
        student: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KycDataEmploymentType.EMPLOYED:
            return employed()
        if self is KycDataEmploymentType.SELF_EMPLOYED:
            return self_employed()
        if self is KycDataEmploymentType.UNEMPLOYED:
            return unemployed()
        if self is KycDataEmploymentType.RETIRED:
            return retired()
        if self is KycDataEmploymentType.STUDENT:
            return student()
