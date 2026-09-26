

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusWhatsAppStatus(enum.StrEnum):
    """
    The status of the message.
    """

    SUBMITTED = "submitted"
    DELIVERED = "delivered"
    REJECTED = "rejected"
    UNDELIVERABLE = "undeliverable"
    READ = "read"

    def visit(
        self,
        submitted: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        undeliverable: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageStatusWhatsAppStatus.SUBMITTED:
            return submitted()
        if self is MessageStatusWhatsAppStatus.DELIVERED:
            return delivered()
        if self is MessageStatusWhatsAppStatus.REJECTED:
            return rejected()
        if self is MessageStatusWhatsAppStatus.UNDELIVERABLE:
            return undeliverable()
        if self is MessageStatusWhatsAppStatus.READ:
            return read()
