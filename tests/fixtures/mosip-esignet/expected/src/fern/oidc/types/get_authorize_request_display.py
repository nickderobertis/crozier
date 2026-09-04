

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthorizeRequestDisplay(enum.StrEnum):
    PAGE = "page"
    POPUP = "popup"
    TOUCH = "touch"
    WAP = "wap"

    def visit(
        self,
        page: typing.Callable[[], T_Result],
        popup: typing.Callable[[], T_Result],
        touch: typing.Callable[[], T_Result],
        wap: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAuthorizeRequestDisplay.PAGE:
            return page()
        if self is GetAuthorizeRequestDisplay.POPUP:
            return popup()
        if self is GetAuthorizeRequestDisplay.TOUCH:
            return touch()
        if self is GetAuthorizeRequestDisplay.WAP:
            return wap()
