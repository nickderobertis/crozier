

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetClientsRequestSortItem(enum.StrEnum):
    DISPLAY_NAME = "display_name"
    DISPLAY_NAME = "-display_name"
    CREATED_AT = "created_at"
    CREATED_AT = "-created_at"

    def visit(self, display_name: typing.Callable[[], T_Result], created_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetClientsRequestSortItem.DISPLAY_NAME:
            return display_name()
        if self is GetClientsRequestSortItem.DISPLAY_NAME:
            return display_name()
        if self is GetClientsRequestSortItem.CREATED_AT:
            return created_at()
        if self is GetClientsRequestSortItem.CREATED_AT:
            return created_at()
