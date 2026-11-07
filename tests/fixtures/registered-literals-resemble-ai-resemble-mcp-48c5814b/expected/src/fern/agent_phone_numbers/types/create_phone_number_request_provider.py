

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreatePhoneNumberRequestProvider(enum.StrEnum):
    TWILIO = "twilio"

    def visit(self, twilio: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreatePhoneNumberRequestProvider.TWILIO:
            return twilio()
