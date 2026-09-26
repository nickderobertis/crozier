

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConsentGrantAllowedChannelsItem(enum.StrEnum):
    EMAIL = "email"
    PHONE = "phone"
    SMS = "sms"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsentGrantAllowedChannelsItem.EMAIL:
            return email()
        if self is ConsentGrantAllowedChannelsItem.PHONE:
            return phone()
        if self is ConsentGrantAllowedChannelsItem.SMS:
            return sms()
