

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DialectHidesWhenKind(enum.StrEnum):
    DIALECT = "dialect"

    def visit(self, dialect: typing.Callable[[], T_Result]) -> T_Result:
        if self is DialectHidesWhenKind.DIALECT:
            return dialect()
