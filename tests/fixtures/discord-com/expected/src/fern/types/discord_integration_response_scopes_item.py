

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DiscordIntegrationResponseScopesItem(enum.StrEnum):
    APPLICATIONS_COMMANDS = "applications.commands"
    BOT = "bot"
    WEBHOOK_INCOMING = "webhook.incoming"

    def visit(
        self,
        applications_commands: typing.Callable[[], T_Result],
        bot: typing.Callable[[], T_Result],
        webhook_incoming: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DiscordIntegrationResponseScopesItem.APPLICATIONS_COMMANDS:
            return applications_commands()
        if self is DiscordIntegrationResponseScopesItem.BOT:
            return bot()
        if self is DiscordIntegrationResponseScopesItem.WEBHOOK_INCOMING:
            return webhook_incoming()
