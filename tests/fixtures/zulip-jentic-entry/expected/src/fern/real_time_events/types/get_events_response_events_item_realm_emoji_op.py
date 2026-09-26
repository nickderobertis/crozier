

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemRealmEmojiOp(enum.StrEnum):
    UPDATE = "update"

    def visit(self, update: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemRealmEmojiOp.UPDATE:
            return update()
