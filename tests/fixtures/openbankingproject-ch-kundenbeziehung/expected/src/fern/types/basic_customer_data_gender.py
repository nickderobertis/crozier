

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BasicCustomerDataGender(enum.StrEnum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"
    UNKNOWN = "unknown"

    def visit(
        self,
        male: typing.Callable[[], T_Result],
        female: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BasicCustomerDataGender.MALE:
            return male()
        if self is BasicCustomerDataGender.FEMALE:
            return female()
        if self is BasicCustomerDataGender.OTHER:
            return other()
        if self is BasicCustomerDataGender.UNKNOWN:
            return unknown()
