

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFleetEventsRequestFormat(enum.StrEnum):
    JSON = "json"
    CSV = "csv"

    def visit(self, json: typing.Callable[[], T_Result], csv: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetFleetEventsRequestFormat.JSON:
            return json()
        if self is GetFleetEventsRequestFormat.CSV:
            return csv()
