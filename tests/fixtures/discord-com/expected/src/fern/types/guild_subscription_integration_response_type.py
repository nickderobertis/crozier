

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GuildSubscriptionIntegrationResponseType(enum.StrEnum):
    GUILD_SUBSCRIPTION = "guild_subscription"

    def visit(self, guild_subscription: typing.Callable[[], T_Result]) -> T_Result:
        if self is GuildSubscriptionIntegrationResponseType.GUILD_SUBSCRIPTION:
            return guild_subscription()
