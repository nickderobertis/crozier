

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes6(enum.StrEnum):
    FRAGMENT_OUTPUT_DEFINITION = "FragmentOutputDefinition"

    def visit(self, fragment_output_definition: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes6.FRAGMENT_OUTPUT_DEFINITION:
            return fragment_output_definition()
