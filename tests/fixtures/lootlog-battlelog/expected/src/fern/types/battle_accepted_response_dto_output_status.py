

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BattleAcceptedResponseDtoOutputStatus(enum.StrEnum):
    ACCEPTED = "ACCEPTED"

    def visit(self, accepted: typing.Callable[[], T_Result]) -> T_Result:
        if self is BattleAcceptedResponseDtoOutputStatus.ACCEPTED:
            return accepted()
