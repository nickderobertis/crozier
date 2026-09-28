

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt(enum.StrEnum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        proto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt.JSON:
            return json()
        if self is MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt.MEDIA:
            return media()
        if self is MonitoringLocationsGlobalMetricsScopesListMetricsScopesByMonitoredProjectRequestAlt.PROTO:
            return proto()
