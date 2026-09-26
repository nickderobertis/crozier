

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommandSource(enum.StrEnum):
    COMMAND = "command"
    MCP = "mcp"
    SKILL = "skill"

    def visit(
        self,
        command: typing.Callable[[], T_Result],
        mcp: typing.Callable[[], T_Result],
        skill: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommandSource.COMMAND:
            return command()
        if self is CommandSource.MCP:
            return mcp()
        if self is CommandSource.SKILL:
            return skill()
