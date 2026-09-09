

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error403Message(enum.StrEnum):
    AUTHORIZATION_FAILED_DUE_TO_INSUFFICIENT_PERMISSIONS = "Authorization failed due to insufficient permissions."

    def visit(self, authorization_failed_due_to_insufficient_permissions: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error403Message.AUTHORIZATION_FAILED_DUE_TO_INSUFFICIENT_PERMISSIONS:
            return authorization_failed_due_to_insufficient_permissions()
