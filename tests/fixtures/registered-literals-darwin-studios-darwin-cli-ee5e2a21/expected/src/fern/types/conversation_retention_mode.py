

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConversationRetentionMode(enum.StrEnum):
    DARWIN_MANAGED = "darwin_managed"
    REMOTE_ONLY = "remote_only"

    def visit(
        self, darwin_managed: typing.Callable[[], T_Result], remote_only: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ConversationRetentionMode.DARWIN_MANAGED:
            return darwin_managed()
        if self is ConversationRetentionMode.REMOTE_ONLY:
            return remote_only()
