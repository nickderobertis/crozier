

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuntimeCatalogWorkflowsItem(enum.StrEnum):
    WEEKLY_OPS = "weekly_ops"

    def visit(self, weekly_ops: typing.Callable[[], T_Result]) -> T_Result:
        if self is RuntimeCatalogWorkflowsItem.WEEKLY_OPS:
            return weekly_ops()
