

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemEmojiIdOp(enum.StrEnum):
    UPDATE_ONE = "update_one"

    def visit(self, update_one: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemEmojiIdOp.UPDATE_ONE:
            return update_one()
