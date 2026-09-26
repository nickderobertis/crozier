

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConversationTitleStatus(enum.StrEnum):
    AUTO_PENDING = "auto_pending"
    AUTO = "auto"
    MANUAL = "manual"

    def visit(
        self,
        auto_pending: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConversationTitleStatus.AUTO_PENDING:
            return auto_pending()
        if self is ConversationTitleStatus.AUTO:
            return auto()
        if self is ConversationTitleStatus.MANUAL:
            return manual()
