

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1ShapeResponseZeroItemHeadersOperation(enum.StrEnum):
    """
    The type of operation performed on the row of the shape.
    """

    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"

    def visit(
        self,
        insert: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetV1ShapeResponseZeroItemHeadersOperation.INSERT:
            return insert()
        if self is GetV1ShapeResponseZeroItemHeadersOperation.UPDATE:
            return update()
        if self is GetV1ShapeResponseZeroItemHeadersOperation.DELETE:
            return delete()
