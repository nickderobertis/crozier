

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt.JSON:
            return json()
        if self is MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt.MEDIA:
            return media()
        if self is MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt.PROTO:
            return proto()
