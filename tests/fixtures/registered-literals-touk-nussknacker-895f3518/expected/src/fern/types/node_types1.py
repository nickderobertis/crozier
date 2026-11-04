

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes1(enum.StrEnum):
    CUSTOM_NODE = "CustomNode"

    def visit(self, custom_node: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes1.CUSTOM_NODE:
            return custom_node()
