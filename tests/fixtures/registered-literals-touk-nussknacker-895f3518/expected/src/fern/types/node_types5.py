

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes5(enum.StrEnum):
    FRAGMENT_INPUT_DEFINITION = "FragmentInputDefinition"

    def visit(self, fragment_input_definition: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes5.FRAGMENT_INPUT_DEFINITION:
            return fragment_input_definition()
