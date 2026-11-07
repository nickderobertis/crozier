

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceTierEnum(enum.StrEnum):
    AUTO = "auto"
    DEFAULT = "default"
    FLEX = "flex"
    PRIORITY = "priority"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        default: typing.Callable[[], T_Result],
        flex: typing.Callable[[], T_Result],
        priority: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceTierEnum.AUTO:
            return auto()
        if self is ServiceTierEnum.DEFAULT:
            return default()
        if self is ServiceTierEnum.FLEX:
            return flex()
        if self is ServiceTierEnum.PRIORITY:
            return priority()
