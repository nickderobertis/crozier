

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreviewDataSourceRequestProvider(enum.StrEnum):
    CALENDAR = "calendar"
    RSS = "rss"
    ATOM = "atom"
    JSON = "json"
    CSV = "csv"
    MANUAL = "manual"
    WEATHER = "weather"
    TRANSIT = "transit"
    CAP_ALERTS = "cap_alerts"
    AIR_QUALITY = "air_quality"

    def visit(
        self,
        calendar: typing.Callable[[], T_Result],
        rss: typing.Callable[[], T_Result],
        atom: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        csv: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
        weather: typing.Callable[[], T_Result],
        transit: typing.Callable[[], T_Result],
        cap_alerts: typing.Callable[[], T_Result],
        air_quality: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PreviewDataSourceRequestProvider.CALENDAR:
            return calendar()
        if self is PreviewDataSourceRequestProvider.RSS:
            return rss()
        if self is PreviewDataSourceRequestProvider.ATOM:
            return atom()
        if self is PreviewDataSourceRequestProvider.JSON:
            return json()
        if self is PreviewDataSourceRequestProvider.CSV:
            return csv()
        if self is PreviewDataSourceRequestProvider.MANUAL:
            return manual()
        if self is PreviewDataSourceRequestProvider.WEATHER:
            return weather()
        if self is PreviewDataSourceRequestProvider.TRANSIT:
            return transit()
        if self is PreviewDataSourceRequestProvider.CAP_ALERTS:
            return cap_alerts()
        if self is PreviewDataSourceRequestProvider.AIR_QUALITY:
            return air_quality()
