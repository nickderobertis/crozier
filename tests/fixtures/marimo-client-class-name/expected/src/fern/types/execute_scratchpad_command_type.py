

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExecuteScratchpadCommandType(enum.StrEnum):
    EXECUTE_SCRATCHPAD = "execute-scratchpad"

    def visit(self, execute_scratchpad: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExecuteScratchpadCommandType.EXECUTE_SCRATCHPAD:
            return execute_scratchpad()
