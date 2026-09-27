

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt.JSON:
            return json()
        if self is MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt.MEDIA:
            return media()
        if self is MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt.PROTO:
            return proto()
