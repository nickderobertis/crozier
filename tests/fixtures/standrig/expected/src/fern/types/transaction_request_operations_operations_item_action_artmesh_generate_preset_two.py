

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetTwo(enum.StrEnum):
    EYELID = "eyelid"

    def visit(self, eyelid: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetTwo.EYELID:
            return eyelid()
