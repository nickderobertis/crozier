

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopEventsReportsResponseReport(enum.StrEnum):
    """
    Discriminator identifying the report type.
    """

    TOP_EVENTS = "top_events"

    def visit(self, top_events: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopEventsReportsResponseReport.TOP_EVENTS:
            return top_events()
