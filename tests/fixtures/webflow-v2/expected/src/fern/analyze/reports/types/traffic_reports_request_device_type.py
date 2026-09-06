

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TrafficReportsRequestDeviceType(enum.StrEnum):
    DESKTOP = "desktop"
    MOBILE = "mobile"
    TABLET = "tablet"

    def visit(
        self,
        desktop: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        tablet: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TrafficReportsRequestDeviceType.DESKTOP:
            return desktop()
        if self is TrafficReportsRequestDeviceType.MOBILE:
            return mobile()
        if self is TrafficReportsRequestDeviceType.TABLET:
            return tablet()
