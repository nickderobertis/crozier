

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PhonePhoneType(enum.StrEnum):
    """
    Resolved phone type (ideally from master data).
    """

    DEFAULT = "DEFAULT"
    OFFICE = "OFFICE"
    FAX = "FAX"
    PHONE = "PHONE"

    def visit(
        self,
        default: typing.Callable[[], T_Result],
        office: typing.Callable[[], T_Result],
        fax: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PhonePhoneType.DEFAULT:
            return default()
        if self is PhonePhoneType.OFFICE:
            return office()
        if self is PhonePhoneType.FAX:
            return fax()
        if self is PhonePhoneType.PHONE:
            return phone()
