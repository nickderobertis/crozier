

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchUsersUserIdBalloonsIdRequestColor(enum.StrEnum):
    BLUE = "blue"
    GREEN = "green"
    RED = "red"

    def visit(
        self,
        blue: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchUsersUserIdBalloonsIdRequestColor.BLUE:
            return blue()
        if self is PatchUsersUserIdBalloonsIdRequestColor.GREEN:
            return green()
        if self is PatchUsersUserIdBalloonsIdRequestColor.RED:
            return red()
