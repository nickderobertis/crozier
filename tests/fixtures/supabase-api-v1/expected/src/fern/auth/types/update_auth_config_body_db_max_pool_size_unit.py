

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateAuthConfigBodyDbMaxPoolSizeUnit(enum.StrEnum):
    CONNECTIONS = "connections"
    PERCENT = "percent"

    def visit(self, connections: typing.Callable[[], T_Result], percent: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateAuthConfigBodyDbMaxPoolSizeUnit.CONNECTIONS:
            return connections()
        if self is UpdateAuthConfigBodyDbMaxPoolSizeUnit.PERCENT:
            return percent()
