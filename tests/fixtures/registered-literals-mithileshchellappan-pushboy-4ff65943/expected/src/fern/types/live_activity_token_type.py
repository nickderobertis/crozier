

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LiveActivityTokenType(enum.StrEnum):
    START = "start"
    UPDATE = "update"

    def visit(self, start: typing.Callable[[], T_Result], update: typing.Callable[[], T_Result]) -> T_Result:
        if self is LiveActivityTokenType.START:
            return start()
        if self is LiveActivityTokenType.UPDATE:
            return update()
