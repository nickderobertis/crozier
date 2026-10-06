

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactPointSystem(enum.StrEnum):
    PHONE = "PHONE"
    FAX = "FAX"
    EMAIL = "EMAIL"
    PAGER = "PAGER"
    URL = "URL"
    SMS = "SMS"
    OTHER = "OTHER"
    NULL = "NULL"

    def visit(
        self,
        phone: typing.Callable[[], T_Result],
        fax: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        pager: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactPointSystem.PHONE:
            return phone()
        if self is ContactPointSystem.FAX:
            return fax()
        if self is ContactPointSystem.EMAIL:
            return email()
        if self is ContactPointSystem.PAGER:
            return pager()
        if self is ContactPointSystem.URL:
            return url()
        if self is ContactPointSystem.SMS:
            return sms()
        if self is ContactPointSystem.OTHER:
            return other()
        if self is ContactPointSystem.NULL:
            return null()
