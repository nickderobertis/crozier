

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt.JSON:
            return json()
        if self is MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt.MEDIA:
            return media()
        if self is MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt.PROTO:
            return proto()
