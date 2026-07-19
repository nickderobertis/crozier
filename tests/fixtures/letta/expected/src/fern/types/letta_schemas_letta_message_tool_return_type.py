

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LettaSchemasLettaMessageToolReturnType(enum.StrEnum):
    """
    The message type to be created.
    """

    TOOL = "tool"

    def visit(self, tool: typing.Callable[[], T_Result]) -> T_Result:
        if self is LettaSchemasLettaMessageToolReturnType.TOOL:
            return tool()
