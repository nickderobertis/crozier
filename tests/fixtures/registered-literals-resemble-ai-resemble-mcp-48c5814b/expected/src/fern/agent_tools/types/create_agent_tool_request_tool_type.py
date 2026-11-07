

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAgentToolRequestToolType(enum.StrEnum):
    WEBHOOK = "webhook"
    CLIENT = "client"

    def visit(self, webhook: typing.Callable[[], T_Result], client: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateAgentToolRequestToolType.WEBHOOK:
            return webhook()
        if self is CreateAgentToolRequestToolType.CLIENT:
            return client()
