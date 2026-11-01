

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrowserImplementationStatus(enum.StrEnum):
    UNAVAILABLE = "unavailable"
    AVAILABLE = "available"

    def visit(self, unavailable: typing.Callable[[], T_Result], available: typing.Callable[[], T_Result]) -> T_Result:
        if self is BrowserImplementationStatus.UNAVAILABLE:
            return unavailable()
        if self is BrowserImplementationStatus.AVAILABLE:
            return available()
