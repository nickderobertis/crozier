

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MessageStatus(str, enum.Enum):
    """
    Status of the delivery of the message.
    """

    ACCEPTED = "accepted"
    SCHEDULED = "scheduled"
    CANCELED = "canceled"
    QUEUED = "queued"
    SENDING = "sending"
    SENT = "sent"
    FAILED = "failed"
    DELIVERED = "delivered"
    UNDELIVERED = "undelivered"
    RECEIVING = "receiving"
    RECEIVED = "received"
    READ = "read"

    def visit(
        self,
        accepted: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        sending: typing.Callable[[], T_Result],
        sent: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        undelivered: typing.Callable[[], T_Result],
        receiving: typing.Callable[[], T_Result],
        received: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageStatus.ACCEPTED:
            return accepted()
        if self is MessageStatus.SCHEDULED:
            return scheduled()
        if self is MessageStatus.CANCELED:
            return canceled()
        if self is MessageStatus.QUEUED:
            return queued()
        if self is MessageStatus.SENDING:
            return sending()
        if self is MessageStatus.SENT:
            return sent()
        if self is MessageStatus.FAILED:
            return failed()
        if self is MessageStatus.DELIVERED:
            return delivered()
        if self is MessageStatus.UNDELIVERED:
            return undelivered()
        if self is MessageStatus.RECEIVING:
            return receiving()
        if self is MessageStatus.RECEIVED:
            return received()
        if self is MessageStatus.READ:
            return read()
