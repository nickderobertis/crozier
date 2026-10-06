

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecordingSnapshotSourceTwo(enum.StrEnum):
    UNKNOWN = "unknown"

    def visit(self, unknown: typing.Callable[[], T_Result]) -> T_Result:
        if self is RecordingSnapshotSourceTwo.UNKNOWN:
            return unknown()
