

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsImportFrom202ResponseTag(enum.StrEnum):
    IMPORTED = "imported"
    DEDUPED = "deduped"
    ACCEPTED = "accepted"

    def visit(
        self,
        imported: typing.Callable[[], T_Result],
        deduped: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentsImportFrom202ResponseTag.IMPORTED:
            return imported()
        if self is DocumentsImportFrom202ResponseTag.DEDUPED:
            return deduped()
        if self is DocumentsImportFrom202ResponseTag.ACCEPTED:
            return accepted()
