

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkDeliverySessionStatus(enum.StrEnum):
    """
    The status of the given Link Delivery Session.

    `CREATED`: The session is created but not yet accessed by the user

    `OPENED`: The session is opened by the user but not yet completed

    `COMPLETED`: The session has been completed by the user

    `EXPIRED`: The session has expired
    """

    CREATED = "CREATED"
    OPENED = "OPENED"
    COMPLETED = "COMPLETED"
    EXPIRED = "EXPIRED"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        opened: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LinkDeliverySessionStatus.CREATED:
            return created()
        if self is LinkDeliverySessionStatus.OPENED:
            return opened()
        if self is LinkDeliverySessionStatus.COMPLETED:
            return completed()
        if self is LinkDeliverySessionStatus.EXPIRED:
            return expired()
