

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class CaptionMediaResponseStatus(enum.StrEnum):
    DONE = "done"
    QUEUED = "queued"

    def visit(self, done: typing.Callable[[], T_Result], queued: typing.Callable[[], T_Result]) -> T_Result:
        if self is CaptionMediaResponseStatus.DONE:
            return done()
        if self is CaptionMediaResponseStatus.QUEUED:
            return queued()
