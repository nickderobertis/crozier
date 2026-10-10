

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpServerApprovalToolSelectorZero(enum.StrEnum):
    ALL = "@all"
    WRITE = "@write"
    DESTRUCTIVE = "@destructive"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        destructive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is McpServerApprovalToolSelectorZero.ALL:
            return all_()
        if self is McpServerApprovalToolSelectorZero.WRITE:
            return write()
        if self is McpServerApprovalToolSelectorZero.DESTRUCTIVE:
            return destructive()
