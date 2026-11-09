

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DfuStateType(enum.StrEnum):
    CARD = "card"
    USER = "user"

    def visit(self, card: typing.Callable[[], T_Result], user: typing.Callable[[], T_Result]) -> T_Result:
        if self is DfuStateType.CARD:
            return card()
        if self is DfuStateType.USER:
            return user()
