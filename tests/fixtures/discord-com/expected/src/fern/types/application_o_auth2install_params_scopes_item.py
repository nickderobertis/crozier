

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicationOAuth2InstallParamsScopesItem(enum.StrEnum):
    APPLICATIONS_COMMANDS = "applications.commands"
    BOT = "bot"

    def visit(
        self, applications_commands: typing.Callable[[], T_Result], bot: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ApplicationOAuth2InstallParamsScopesItem.APPLICATIONS_COMMANDS:
            return applications_commands()
        if self is ApplicationOAuth2InstallParamsScopesItem.BOT:
            return bot()
