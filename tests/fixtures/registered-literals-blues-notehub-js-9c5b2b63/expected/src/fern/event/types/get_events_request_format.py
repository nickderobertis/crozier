

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsRequestFormat(enum.StrEnum):
    JSON = "json"
    CSV = "csv"

    def visit(self, json: typing.Callable[[], T_Result], csv: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsRequestFormat.JSON:
            return json()
        if self is GetEventsRequestFormat.CSV:
            return csv()
