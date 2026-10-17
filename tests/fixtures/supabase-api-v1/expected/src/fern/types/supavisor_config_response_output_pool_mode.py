

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SupavisorConfigResponseOutputPoolMode(enum.StrEnum):
    TRANSACTION = "transaction"
    SESSION = "session"

    def visit(self, transaction: typing.Callable[[], T_Result], session: typing.Callable[[], T_Result]) -> T_Result:
        if self is SupavisorConfigResponseOutputPoolMode.TRANSACTION:
            return transaction()
        if self is SupavisorConfigResponseOutputPoolMode.SESSION:
            return session()
