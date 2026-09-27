

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionPartContourShadeShadeProfile(enum.StrEnum):
    CHEEK = "cheek"

    def visit(self, cheek: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionPartContourShadeShadeProfile.CHEEK:
            return cheek()
