

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes7(enum.StrEnum):
    JOIN = "Join"

    def visit(self, join: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes7.JOIN:
            return join()
