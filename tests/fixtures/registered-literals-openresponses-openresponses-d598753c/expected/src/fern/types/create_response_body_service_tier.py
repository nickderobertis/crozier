

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateResponseBodyServiceTier(enum.StrEnum):
    """
    The service tier to use for this request.
    """

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
        if self is CreateResponseBodyServiceTier.AUTO:
            return auto()
        if self is CreateResponseBodyServiceTier.DEFAULT:
            return default()
        if self is CreateResponseBodyServiceTier.FLEX:
            return flex()
        if self is CreateResponseBodyServiceTier.PRIORITY:
            return priority()
