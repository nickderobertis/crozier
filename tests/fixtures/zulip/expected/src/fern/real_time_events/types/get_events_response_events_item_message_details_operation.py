

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemMessageDetailsOperation(enum.StrEnum):
    """
    Old name for the `op` field in this event type.

    **Deprecated** in Zulip 4.0 (feature level 32), and
    replaced by the `op` field.
    """

    REMOVE = "remove"

    def visit(self, remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemMessageDetailsOperation.REMOVE:
            return remove()
