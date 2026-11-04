

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExporterInfoContextType(enum.StrEnum):
    NONE = "NONE"
    AUTO = "AUTO"
    CUSTOM = "CUSTOM"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExporterInfoContextType.NONE:
            return none()
        if self is ExporterInfoContextType.AUTO:
            return auto()
        if self is ExporterInfoContextType.CUSTOM:
            return custom()
