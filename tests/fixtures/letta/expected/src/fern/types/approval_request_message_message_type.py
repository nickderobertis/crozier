

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApprovalRequestMessageMessageType(enum.StrEnum):
    """
    The type of the message.
    """

    APPROVAL_REQUEST_MESSAGE = "approval_request_message"

    def visit(self, approval_request_message: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApprovalRequestMessageMessageType.APPROVAL_REQUEST_MESSAGE:
            return approval_request_message()
