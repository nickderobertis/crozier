

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt.JSON:
            return json()
        if self is MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt.MEDIA:
            return media()
        if self is MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt.PROTO:
            return proto()
