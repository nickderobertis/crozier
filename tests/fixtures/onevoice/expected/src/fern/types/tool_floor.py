

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolFloor(enum.StrEnum):
    """
    Per-tool HITL floor (strictness: auto < manual < forbidden).
    Business-level approvals only persist `auto` / `manual`;
    `forbidden` is reserved for tool-registry defaults.
    """

    AUTO = "auto"
    MANUAL = "manual"
    FORBIDDEN = "forbidden"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolFloor.AUTO:
            return auto()
        if self is ToolFloor.MANUAL:
            return manual()
        if self is ToolFloor.FORBIDDEN:
            return forbidden()
