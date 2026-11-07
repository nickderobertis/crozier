

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InnerErrorCode(enum.StrEnum):
    """
    Inner error codes as defined in the Microsoft REST guidelines
    (https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses).
    """

    INVALID_PAYLOAD = "invalidPayload"

    def visit(self, invalid_payload: typing.Callable[[], T_Result]) -> T_Result:
        if self is InnerErrorCode.INVALID_PAYLOAD:
            return invalid_payload()
