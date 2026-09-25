

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CollectionDocumentInfoStrType(enum.StrEnum):
    """
    The collection type.
    """

    DOCUMENT = "Document"

    def visit(self, document: typing.Callable[[], T_Result]) -> T_Result:
        if self is CollectionDocumentInfoStrType.DOCUMENT:
            return document()
