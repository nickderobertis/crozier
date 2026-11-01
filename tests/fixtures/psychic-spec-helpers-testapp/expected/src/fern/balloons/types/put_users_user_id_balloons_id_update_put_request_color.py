

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutUsersUserIdBalloonsIdUpdatePutRequestColor(enum.StrEnum):
    BLUE = "blue"
    GREEN = "green"
    RED = "red"

    def visit(
        self,
        blue: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutUsersUserIdBalloonsIdUpdatePutRequestColor.BLUE:
            return blue()
        if self is PutUsersUserIdBalloonsIdUpdatePutRequestColor.GREEN:
            return green()
        if self is PutUsersUserIdBalloonsIdUpdatePutRequestColor.RED:
            return red()
