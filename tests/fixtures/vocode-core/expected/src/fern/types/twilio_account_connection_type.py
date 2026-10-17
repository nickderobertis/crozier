

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TwilioAccountConnectionType(enum.StrEnum):
    ACCOUNT_CONNECTION_TWILIO = "account_connection_twilio"

    def visit(self, account_connection_twilio: typing.Callable[[], T_Result]) -> T_Result:
        if self is TwilioAccountConnectionType.ACCOUNT_CONNECTION_TWILIO:
            return account_connection_twilio()
