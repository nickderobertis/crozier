

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StringSelectFormFieldFormFactor(enum.StrEnum):
    CLOUD_SELECT = "CLOUD_SELECT"
    SELECT_MENU = "SELECT_MENU"

    def visit(
        self, cloud_select: typing.Callable[[], T_Result], select_menu: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is StringSelectFormFieldFormFactor.CLOUD_SELECT:
            return cloud_select()
        if self is StringSelectFormFieldFormFactor.SELECT_MENU:
            return select_menu()
