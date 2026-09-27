

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestRigKind(enum.StrEnum):
    IMPORT = "import"

    def visit(self, import_: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestRigKind.IMPORT:
            return import_()
