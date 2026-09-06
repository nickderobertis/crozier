

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetKnownPageHashesRequestActionItem(enum.StrEnum):
    DELETE_AUTO = "DELETE_AUTO"
    DELETE_MANUAL = "DELETE_MANUAL"
    IGNORE = "IGNORE"

    def visit(
        self,
        delete_auto: typing.Callable[[], T_Result],
        delete_manual: typing.Callable[[], T_Result],
        ignore: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetKnownPageHashesRequestActionItem.DELETE_AUTO:
            return delete_auto()
        if self is GetKnownPageHashesRequestActionItem.DELETE_MANUAL:
            return delete_manual()
        if self is GetKnownPageHashesRequestActionItem.IGNORE:
            return ignore()
