

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InspectDataSourceRequestProvider(enum.StrEnum):
    RSS = "rss"
    ATOM = "atom"
    JSON = "json"
    CSV = "csv"

    def visit(
        self,
        rss: typing.Callable[[], T_Result],
        atom: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        csv: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InspectDataSourceRequestProvider.RSS:
            return rss()
        if self is InspectDataSourceRequestProvider.ATOM:
            return atom()
        if self is InspectDataSourceRequestProvider.JSON:
            return json()
        if self is InspectDataSourceRequestProvider.CSV:
            return csv()
