

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VersionMismatchResponseCode(enum.StrEnum):
    VERSION_MISMATCH = "version_mismatch"

    def visit(self, version_mismatch: typing.Callable[[], T_Result]) -> T_Result:
        if self is VersionMismatchResponseCode.VERSION_MISMATCH:
            return version_mismatch()
