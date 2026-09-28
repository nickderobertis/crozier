

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2BulkDeleteTablesDataFailedItemKind(enum.StrEnum):
    """
    Which kind of item this entry names.
    """

    TABLE = "table"
    FOLDER = "folder"

    def visit(self, table: typing.Callable[[], T_Result], folder: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2BulkDeleteTablesDataFailedItemKind.TABLE:
            return table()
        if self is V2BulkDeleteTablesDataFailedItemKind.FOLDER:
            return folder()
