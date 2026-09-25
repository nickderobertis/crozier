

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MuteTopicRequestOp(enum.StrEnum):
    """
    Whether to mute (`add`) or unmute (`remove`) the provided topic.
    """

    ADD = "add"
    REMOVE = "remove"

    def visit(self, add: typing.Callable[[], T_Result], remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is MuteTopicRequestOp.ADD:
            return add()
        if self is MuteTopicRequestOp.REMOVE:
            return remove()
