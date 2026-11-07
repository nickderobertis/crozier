

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TelemetryMetricsRequestType(enum.StrEnum):
    SOURCE = "source"
    URL = "url"
    EVENT = "event"
    REFERRER = "referrer"
    COUNTRY = "country"

    def visit(
        self,
        source: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
        referrer: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TelemetryMetricsRequestType.SOURCE:
            return source()
        if self is TelemetryMetricsRequestType.URL:
            return url()
        if self is TelemetryMetricsRequestType.EVENT:
            return event()
        if self is TelemetryMetricsRequestType.REFERRER:
            return referrer()
        if self is TelemetryMetricsRequestType.COUNTRY:
            return country()
