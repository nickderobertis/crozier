

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WalletConnectBlockGroupType(enum.StrEnum):
    QUESTION = "QUESTION"

    def visit(self, question: typing.Callable[[], T_Result]) -> T_Result:
        if self is WalletConnectBlockGroupType.QUESTION:
            return question()
