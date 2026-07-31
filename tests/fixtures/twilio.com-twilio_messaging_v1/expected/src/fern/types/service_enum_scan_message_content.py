

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceEnumScanMessageContent(enum.StrEnum):
    INHERIT = "inherit"
    ENABLE = "enable"
    DISABLE = "disable"

    def visit(
        self,
        inherit: typing.Callable[[], T_Result],
        enable: typing.Callable[[], T_Result],
        disable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceEnumScanMessageContent.INHERIT:
            return inherit()
        if self is ServiceEnumScanMessageContent.ENABLE:
            return enable()
        if self is ServiceEnumScanMessageContent.DISABLE:
            return disable()
