

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSupavisorConfigBodyPoolMode(enum.StrEnum):
    """
    Dedicated pooler mode for the project
    """

    TRANSACTION = "transaction"
    SESSION = "session"

    def visit(self, transaction: typing.Callable[[], T_Result], session: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateSupavisorConfigBodyPoolMode.TRANSACTION:
            return transaction()
        if self is UpdateSupavisorConfigBodyPoolMode.SESSION:
            return session()
