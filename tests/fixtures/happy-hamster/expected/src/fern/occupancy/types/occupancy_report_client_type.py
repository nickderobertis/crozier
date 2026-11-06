

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class OccupancyReportClientType(enum.StrEnum):
    """
    Type of the client which reported the occupancy
    """

    IOT = "IOT"
    WEB_APP = "WEB_APP"

    def visit(self, iot: typing.Callable[[], T_Result], web_app: typing.Callable[[], T_Result]) -> T_Result:
        if self is OccupancyReportClientType.IOT:
            return iot()
        if self is OccupancyReportClientType.WEB_APP:
            return web_app()
