

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaybackDiagnosticsNodesItemSourcesItemKind(enum.StrEnum):
    BOT = "bot"
    ACCOUNT = "account"
    LOCAL = "local"

    def visit(
        self,
        bot: typing.Callable[[], T_Result],
        account: typing.Callable[[], T_Result],
        local: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlaybackDiagnosticsNodesItemSourcesItemKind.BOT:
            return bot()
        if self is PlaybackDiagnosticsNodesItemSourcesItemKind.ACCOUNT:
            return account()
        if self is PlaybackDiagnosticsNodesItemSourcesItemKind.LOCAL:
            return local()
