

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RefreshTelegramResponseLinkedGroupStatus(enum.StrEnum):
    OK = "ok"
    BOT_NOT_MEMBER = "bot_not_member"
    NO_LINKED_GROUP = "no_linked_group"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        bot_not_member: typing.Callable[[], T_Result],
        no_linked_group: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RefreshTelegramResponseLinkedGroupStatus.OK:
            return ok()
        if self is RefreshTelegramResponseLinkedGroupStatus.BOT_NOT_MEMBER:
            return bot_not_member()
        if self is RefreshTelegramResponseLinkedGroupStatus.NO_LINKED_GROUP:
            return no_linked_group()
