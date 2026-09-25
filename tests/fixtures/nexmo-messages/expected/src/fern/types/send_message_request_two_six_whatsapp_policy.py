

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SendMessageRequestTwoSixWhatsappPolicy(enum.StrEnum):
    """
    Policy for resolving what language template to use. As of right now the only valid choice is `deterministic`.
    """

    DETERMINISTIC = "deterministic"

    def visit(self, deterministic: typing.Callable[[], T_Result]) -> T_Result:
        if self is SendMessageRequestTwoSixWhatsappPolicy.DETERMINISTIC:
            return deterministic()
