

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyOneOperation(enum.StrEnum):
    """
    Old name for the `op` field in this event type.

    **Deprecated** in Zulip 4.0 (feature level 32), and
    replaced by the `op` field.
    """

    ADD = "add"

    def visit(self, add: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyOneOperation.ADD:
            return add()
