

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsAnalysis200ResponseRestrictionsItemSource(enum.StrEnum):
    DOCMDP = "docmdp"
    FIELDMDP = "fieldmdp"
    LOCK = "lock"

    def visit(
        self,
        docmdp: typing.Callable[[], T_Result],
        fieldmdp: typing.Callable[[], T_Result],
        lock: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocVersionsAnalysis200ResponseRestrictionsItemSource.DOCMDP:
            return docmdp()
        if self is DocVersionsAnalysis200ResponseRestrictionsItemSource.FIELDMDP:
            return fieldmdp()
        if self is DocVersionsAnalysis200ResponseRestrictionsItemSource.LOCK:
            return lock()
