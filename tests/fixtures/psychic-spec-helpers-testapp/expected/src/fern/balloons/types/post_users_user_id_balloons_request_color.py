

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostUsersUserIdBalloonsRequestColor(enum.StrEnum):
    BLUE = "blue"
    GREEN = "green"
    RED = "red"

    def visit(
        self,
        blue: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostUsersUserIdBalloonsRequestColor.BLUE:
            return blue()
        if self is PostUsersUserIdBalloonsRequestColor.GREEN:
            return green()
        if self is PostUsersUserIdBalloonsRequestColor.RED:
            return red()
