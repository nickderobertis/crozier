

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class EndWatchRequestWatchIdOne(enum.StrEnum):
    EVERY = "every"

    def visit(self, every: typing.Callable[[], T_Result]) -> T_Result:
        if self is EndWatchRequestWatchIdOne.EVERY:
            return every()
