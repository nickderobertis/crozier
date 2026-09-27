

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt.JSON:
            return json()
        if self is MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt.MEDIA:
            return media()
        if self is MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt.PROTO:
            return proto()
