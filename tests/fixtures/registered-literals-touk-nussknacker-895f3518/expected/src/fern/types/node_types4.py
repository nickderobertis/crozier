

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes4(enum.StrEnum):
    FRAGMENT_INPUT = "FragmentInput"

    def visit(self, fragment_input: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes4.FRAGMENT_INPUT:
            return fragment_input()
