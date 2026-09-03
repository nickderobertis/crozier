

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PurposeType(enum.StrEnum):
    NONE = "none"
    VERIFY = "verify"
    LINK = "link"
    LOGIN = "login"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        verify: typing.Callable[[], T_Result],
        link: typing.Callable[[], T_Result],
        login: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PurposeType.NONE:
            return none()
        if self is PurposeType.VERIFY:
            return verify()
        if self is PurposeType.LINK:
            return link()
        if self is PurposeType.LOGIN:
            return login()
