

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PhoneType(enum.StrEnum):
    """
    An enum indicating whether a phone number is a phone line or a fax line.
    """

    PHONE = "phone"
    FAX = "fax"

    def visit(self, phone: typing.Callable[[], T_Result], fax: typing.Callable[[], T_Result]) -> T_Result:
        if self is PhoneType.PHONE:
            return phone()
        if self is PhoneType.FAX:
            return fax()
