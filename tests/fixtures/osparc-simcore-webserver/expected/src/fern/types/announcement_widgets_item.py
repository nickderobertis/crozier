

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnnouncementWidgetsItem(enum.StrEnum):
    LOGIN = "login"
    RIBBON = "ribbon"
    USER_MENU = "user-menu"

    def visit(
        self,
        login: typing.Callable[[], T_Result],
        ribbon: typing.Callable[[], T_Result],
        user_menu: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AnnouncementWidgetsItem.LOGIN:
            return login()
        if self is AnnouncementWidgetsItem.RIBBON:
            return ribbon()
        if self is AnnouncementWidgetsItem.USER_MENU:
            return user_menu()
