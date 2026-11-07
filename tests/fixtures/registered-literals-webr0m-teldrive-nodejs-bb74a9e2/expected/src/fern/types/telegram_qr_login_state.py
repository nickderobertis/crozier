

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TelegramQrLoginState(enum.StrEnum):
    PENDING = "pending"
    PASSWORD_REQUIRED = "password_required"

    def visit(
        self, pending: typing.Callable[[], T_Result], password_required: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TelegramQrLoginState.PENDING:
            return pending()
        if self is TelegramQrLoginState.PASSWORD_REQUIRED:
            return password_required()
