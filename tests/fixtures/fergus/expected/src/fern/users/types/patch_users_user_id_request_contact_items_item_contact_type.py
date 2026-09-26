

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchUsersUserIdRequestContactItemsItemContactType(enum.StrEnum):
    """
    The type of this contact item. It can be one of the following: phone, mobile, fax, other, website
    """

    PHONE = "phone"
    MOBILE = "mobile"
    OTHER = "other"
    FAX = "fax"
    WEBSITE = "website"

    def visit(
        self,
        phone: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        fax: typing.Callable[[], T_Result],
        website: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchUsersUserIdRequestContactItemsItemContactType.PHONE:
            return phone()
        if self is PatchUsersUserIdRequestContactItemsItemContactType.MOBILE:
            return mobile()
        if self is PatchUsersUserIdRequestContactItemsItemContactType.OTHER:
            return other()
        if self is PatchUsersUserIdRequestContactItemsItemContactType.FAX:
            return fax()
        if self is PatchUsersUserIdRequestContactItemsItemContactType.WEBSITE:
            return website()
