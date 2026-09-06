

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopEventsReportsRequestDeviceType(enum.StrEnum):
    DESKTOP = "desktop"
    MOBILE = "mobile"
    TABLET = "tablet"

    def visit(
        self,
        desktop: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        tablet: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TopEventsReportsRequestDeviceType.DESKTOP:
            return desktop()
        if self is TopEventsReportsRequestDeviceType.MOBILE:
            return mobile()
        if self is TopEventsReportsRequestDeviceType.TABLET:
            return tablet()
