

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableJobStateType(enum.StrEnum):
    IMPORT = "import"
    DELETE = "delete"
    EXPORT = "export"
    BACKFILL = "backfill"
    UPDATE = "update"

    def visit(
        self,
        import_: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        export: typing.Callable[[], T_Result],
        backfill: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2TableJobStateType.IMPORT:
            return import_()
        if self is V2TableJobStateType.DELETE:
            return delete()
        if self is V2TableJobStateType.EXPORT:
            return export()
        if self is V2TableJobStateType.BACKFILL:
            return backfill()
        if self is V2TableJobStateType.UPDATE:
            return update()
