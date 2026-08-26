

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnvironmentVariableDiscoveryValueKind(enum.StrEnum):
    ENVIRONMENT_VARIABLE = "environment-variable"

    def visit(self, environment_variable: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnvironmentVariableDiscoveryValueKind.ENVIRONMENT_VARIABLE:
            return environment_variable()
