

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentParamsEndpointingSensitivity(enum.StrEnum):
    AUTO = "auto"
    RELAXED = "relaxed"
    SENSITIVE = "sensitive"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        relaxed: typing.Callable[[], T_Result],
        sensitive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentParamsEndpointingSensitivity.AUTO:
            return auto()
        if self is AgentParamsEndpointingSensitivity.RELAXED:
            return relaxed()
        if self is AgentParamsEndpointingSensitivity.SENSITIVE:
            return sensitive()
