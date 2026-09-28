

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelIngressListResponseSourcesItemState(enum.StrEnum):
    APPROVED = "approved"
    PENDING = "pending"

    def visit(self, approved: typing.Callable[[], T_Result], pending: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelIngressListResponseSourcesItemState.APPROVED:
            return approved()
        if self is ChannelIngressListResponseSourcesItemState.PENDING:
            return pending()
