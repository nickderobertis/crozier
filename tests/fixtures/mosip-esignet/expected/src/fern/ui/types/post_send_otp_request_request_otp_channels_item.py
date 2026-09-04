

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostSendOtpRequestRequestOtpChannelsItem(enum.StrEnum):
    PHONE = "phone"
    EMAIL = "email"

    def visit(self, phone: typing.Callable[[], T_Result], email: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSendOtpRequestRequestOtpChannelsItem.PHONE:
            return phone()
        if self is PostSendOtpRequestRequestOtpChannelsItem.EMAIL:
            return email()
