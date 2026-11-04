

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpServerToolSelectorZero(enum.StrEnum):
    ALL = "@all"
    READ_ONLY = "@read-only"

    def visit(self, all_: typing.Callable[[], T_Result], read_only: typing.Callable[[], T_Result]) -> T_Result:
        if self is McpServerToolSelectorZero.ALL:
            return all_()
        if self is McpServerToolSelectorZero.READ_ONLY:
            return read_only()
