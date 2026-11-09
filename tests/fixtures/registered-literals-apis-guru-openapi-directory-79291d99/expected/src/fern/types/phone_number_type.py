

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PhoneNumberType(enum.StrEnum):
    """
    The type of phone number.
    """

    HOME = "home"
    WORK = "work"
    OFFICE = "office"
    MOBILE = "mobile"
    MOBILE1 = "mobile1"
    OTHER = "other"

    def visit(
        self,
        home: typing.Callable[[], T_Result],
        work: typing.Callable[[], T_Result],
        office: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        mobile1: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PhoneNumberType.HOME:
            return home()
        if self is PhoneNumberType.WORK:
            return work()
        if self is PhoneNumberType.OFFICE:
            return office()
        if self is PhoneNumberType.MOBILE:
            return mobile()
        if self is PhoneNumberType.MOBILE1:
            return mobile1()
        if self is PhoneNumberType.OTHER:
            return other()
