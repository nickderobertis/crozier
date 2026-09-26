

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsSignatures200ResponseProtectionFieldLocksItemSource(enum.StrEnum):
    FIELDMDP = "fieldmdp"
    LOCK = "lock"

    def visit(self, fieldmdp: typing.Callable[[], T_Result], lock: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocVersionsSignatures200ResponseProtectionFieldLocksItemSource.FIELDMDP:
            return fieldmdp()
        if self is DocVersionsSignatures200ResponseProtectionFieldLocksItemSource.LOCK:
            return lock()
