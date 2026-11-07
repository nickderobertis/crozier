

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentInfoType(enum.StrEnum):
    """
    Subagent kind.
    """

    DYNAMIC = "dynamic"

    def visit(self, dynamic: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentInfoType.DYNAMIC:
            return dynamic()
