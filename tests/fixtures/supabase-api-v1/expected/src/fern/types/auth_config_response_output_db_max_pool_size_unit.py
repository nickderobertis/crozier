

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthConfigResponseOutputDbMaxPoolSizeUnit(enum.StrEnum):
    CONNECTIONS = "connections"
    PERCENT = "percent"

    def visit(self, connections: typing.Callable[[], T_Result], percent: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthConfigResponseOutputDbMaxPoolSizeUnit.CONNECTIONS:
            return connections()
        if self is AuthConfigResponseOutputDbMaxPoolSizeUnit.PERCENT:
            return percent()
