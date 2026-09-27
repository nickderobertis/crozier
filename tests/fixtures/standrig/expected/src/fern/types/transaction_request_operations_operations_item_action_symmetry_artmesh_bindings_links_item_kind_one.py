

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindOne(enum.StrEnum):
    DEFORMER = "deformer"

    def visit(self, deformer: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindOne.DEFORMER:
            return deformer()
