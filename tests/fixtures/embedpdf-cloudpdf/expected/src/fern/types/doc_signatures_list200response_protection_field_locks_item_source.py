

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesList200ResponseProtectionFieldLocksItemSource(enum.StrEnum):
    FIELDMDP = "fieldmdp"
    LOCK = "lock"

    def visit(self, fieldmdp: typing.Callable[[], T_Result], lock: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocSignaturesList200ResponseProtectionFieldLocksItemSource.FIELDMDP:
            return fieldmdp()
        if self is DocSignaturesList200ResponseProtectionFieldLocksItemSource.LOCK:
            return lock()
