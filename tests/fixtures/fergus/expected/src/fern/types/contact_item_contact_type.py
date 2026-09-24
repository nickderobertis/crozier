

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactItemContactType(enum.StrEnum):
    """
    The type of this contact item. It can be one of the following: email, phone, mobile, other, fax, website
    """

    EMAIL = "email"
    PHONE = "phone"
    MOBILE = "mobile"
    OTHER = "other"
    FAX = "fax"
    WEBSITE = "website"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        fax: typing.Callable[[], T_Result],
        website: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactItemContactType.EMAIL:
            return email()
        if self is ContactItemContactType.PHONE:
            return phone()
        if self is ContactItemContactType.MOBILE:
            return mobile()
        if self is ContactItemContactType.OTHER:
            return other()
        if self is ContactItemContactType.FAX:
            return fax()
        if self is ContactItemContactType.WEBSITE:
            return website()
