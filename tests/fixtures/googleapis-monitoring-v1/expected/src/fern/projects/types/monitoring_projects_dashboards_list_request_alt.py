

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsDashboardsListRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitoringProjectsDashboardsListRequestAlt.JSON:
            return json()
        if self is MonitoringProjectsDashboardsListRequestAlt.MEDIA:
            return media()
        if self is MonitoringProjectsDashboardsListRequestAlt.PROTO:
            return proto()
