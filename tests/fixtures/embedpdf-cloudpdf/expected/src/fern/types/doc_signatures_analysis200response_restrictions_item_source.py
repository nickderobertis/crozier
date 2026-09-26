

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesAnalysis200ResponseRestrictionsItemSource(enum.StrEnum):
    DOCMDP = "docmdp"
    FIELDMDP = "fieldmdp"
    LOCK = "lock"

    def visit(
        self,
        docmdp: typing.Callable[[], T_Result],
        fieldmdp: typing.Callable[[], T_Result],
        lock: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocSignaturesAnalysis200ResponseRestrictionsItemSource.DOCMDP:
            return docmdp()
        if self is DocSignaturesAnalysis200ResponseRestrictionsItemSource.FIELDMDP:
            return fieldmdp()
        if self is DocSignaturesAnalysis200ResponseRestrictionsItemSource.LOCK:
            return lock()
