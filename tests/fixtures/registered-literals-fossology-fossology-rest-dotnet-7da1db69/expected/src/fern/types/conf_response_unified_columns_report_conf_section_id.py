

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfResponseUnifiedColumnsReportConfSectionId(enum.StrEnum):
    ON = "on"
    OFF = "off"

    def visit(self, on: typing.Callable[[], T_Result], off: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConfResponseUnifiedColumnsReportConfSectionId.ON:
            return on()
        if self is ConfResponseUnifiedColumnsReportConfSectionId.OFF:
            return off()
