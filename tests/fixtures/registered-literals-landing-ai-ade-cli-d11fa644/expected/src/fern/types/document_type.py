

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentType(enum.StrEnum):
    """
    The node type. Identifies this node as the root of the structure tree.
    """

    DOCUMENT = "document"

    def visit(self, document: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocumentType.DOCUMENT:
            return document()
