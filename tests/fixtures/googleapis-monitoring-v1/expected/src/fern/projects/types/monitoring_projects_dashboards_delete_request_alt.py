

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsDashboardsDeleteRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitoringProjectsDashboardsDeleteRequestAlt.JSON:
            return json()
        if self is MonitoringProjectsDashboardsDeleteRequestAlt.MEDIA:
            return media()
        if self is MonitoringProjectsDashboardsDeleteRequestAlt.PROTO:
            return proto()
