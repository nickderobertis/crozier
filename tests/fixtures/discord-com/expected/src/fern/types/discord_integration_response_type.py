

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DiscordIntegrationResponseType(enum.StrEnum):
    DISCORD = "discord"

    def visit(self, discord: typing.Callable[[], T_Result]) -> T_Result:
        if self is DiscordIntegrationResponseType.DISCORD:
            return discord()
