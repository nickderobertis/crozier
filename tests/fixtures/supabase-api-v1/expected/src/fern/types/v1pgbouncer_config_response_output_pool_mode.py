

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1PgbouncerConfigResponseOutputPoolMode(enum.StrEnum):
    TRANSACTION = "transaction"
    SESSION = "session"
    STATEMENT = "statement"

    def visit(
        self,
        transaction: typing.Callable[[], T_Result],
        session: typing.Callable[[], T_Result],
        statement: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1PgbouncerConfigResponseOutputPoolMode.TRANSACTION:
            return transaction()
        if self is V1PgbouncerConfigResponseOutputPoolMode.SESSION:
            return session()
        if self is V1PgbouncerConfigResponseOutputPoolMode.STATEMENT:
            return statement()
