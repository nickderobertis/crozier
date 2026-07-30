

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PhoneNumberType(enum.StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    HOME = "home"
    WORK = "work"
    OFFICE = "office"
    MOBILE = "mobile"
    ASSISTANT = "assistant"
    FAX = "fax"
    DIRECT_DIAL_IN = "direct-dial-in"
    PERSONAL = "personal"
    OTHER = "other"

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        home: typing.Callable[[], T_Result],
        work: typing.Callable[[], T_Result],
        office: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        fax: typing.Callable[[], T_Result],
        direct_dial_in: typing.Callable[[], T_Result],
        personal: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PhoneNumberType.PRIMARY:
            return primary()
        if self is PhoneNumberType.SECONDARY:
            return secondary()
        if self is PhoneNumberType.HOME:
            return home()
        if self is PhoneNumberType.WORK:
            return work()
        if self is PhoneNumberType.OFFICE:
            return office()
        if self is PhoneNumberType.MOBILE:
            return mobile()
        if self is PhoneNumberType.ASSISTANT:
            return assistant()
        if self is PhoneNumberType.FAX:
            return fax()
        if self is PhoneNumberType.DIRECT_DIAL_IN:
            return direct_dial_in()
        if self is PhoneNumberType.PERSONAL:
            return personal()
        if self is PhoneNumberType.OTHER:
            return other()
