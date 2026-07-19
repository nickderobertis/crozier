

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1ShapeResponseDataDataItemHeadersOperation(enum.StrEnum):
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
        if self is GetV1ShapeResponseDataDataItemHeadersOperation.INSERT:
            return insert()
        if self is GetV1ShapeResponseDataDataItemHeadersOperation.UPDATE:
            return update()
        if self is GetV1ShapeResponseDataDataItemHeadersOperation.DELETE:
            return delete()
