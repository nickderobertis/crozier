

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TelemetryExtensionTypeItem(enum.StrEnum):
    LOCATION = "location"
    MAINTENANCE = "maintenance"

    def visit(self, location: typing.Callable[[], T_Result], maintenance: typing.Callable[[], T_Result]) -> T_Result:
        if self is TelemetryExtensionTypeItem.LOCATION:
            return location()
        if self is TelemetryExtensionTypeItem.MAINTENANCE:
            return maintenance()
