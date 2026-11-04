

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StreamPlaybackRequestDownload(enum.StrEnum):
    ONE = "1"

    def visit(self, one: typing.Callable[[], T_Result]) -> T_Result:
        if self is StreamPlaybackRequestDownload.ONE:
            return one()
