

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactItemPayloadContactType(enum.StrEnum):
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
        if self is ContactItemPayloadContactType.EMAIL:
            return email()
        if self is ContactItemPayloadContactType.PHONE:
            return phone()
        if self is ContactItemPayloadContactType.MOBILE:
            return mobile()
        if self is ContactItemPayloadContactType.OTHER:
            return other()
        if self is ContactItemPayloadContactType.FAX:
            return fax()
        if self is ContactItemPayloadContactType.WEBSITE:
            return website()
