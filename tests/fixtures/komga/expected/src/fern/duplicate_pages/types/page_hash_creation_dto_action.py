

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PageHashCreationDtoAction(enum.StrEnum):
    DELETE_AUTO = "DELETE_AUTO"
    DELETE_MANUAL = "DELETE_MANUAL"
    IGNORE = "IGNORE"

    def visit(
        self,
        delete_auto: typing.Callable[[], T_Result],
        delete_manual: typing.Callable[[], T_Result],
        ignore: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PageHashCreationDtoAction.DELETE_AUTO:
            return delete_auto()
        if self is PageHashCreationDtoAction.DELETE_MANUAL:
            return delete_manual()
        if self is PageHashCreationDtoAction.IGNORE:
            return ignore()
