

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateEmbeddingResponseObject(enum.StrEnum):
    """
    The object type, which is always "list".
    """

    LIST = "list"

    def visit(self, list_: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateEmbeddingResponseObject.LIST:
            return list_()
