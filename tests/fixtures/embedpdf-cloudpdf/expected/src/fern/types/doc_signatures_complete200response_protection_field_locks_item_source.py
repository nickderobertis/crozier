

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesComplete200ResponseProtectionFieldLocksItemSource(enum.StrEnum):
    FIELDMDP = "fieldmdp"
    LOCK = "lock"

    def visit(self, fieldmdp: typing.Callable[[], T_Result], lock: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocSignaturesComplete200ResponseProtectionFieldLocksItemSource.FIELDMDP:
            return fieldmdp()
        if self is DocSignaturesComplete200ResponseProtectionFieldLocksItemSource.LOCK:
            return lock()
