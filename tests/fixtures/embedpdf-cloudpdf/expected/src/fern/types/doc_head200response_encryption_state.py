

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocHead200ResponseEncryptionState(enum.StrEnum):
    UNKNOWN = "unknown"
    NONE = "none"
    ENCRYPTED = "encrypted"
    UNSUPPORTED = "unsupported"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        encrypted: typing.Callable[[], T_Result],
        unsupported: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocHead200ResponseEncryptionState.UNKNOWN:
            return unknown()
        if self is DocHead200ResponseEncryptionState.NONE:
            return none()
        if self is DocHead200ResponseEncryptionState.ENCRYPTED:
            return encrypted()
        if self is DocHead200ResponseEncryptionState.UNSUPPORTED:
            return unsupported()
