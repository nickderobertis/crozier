

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TrustedKeyResponseDtoAudience(enum.StrEnum):
    HUMAN = "human"
    CLIENT = "client"

    def visit(self, human: typing.Callable[[], T_Result], client: typing.Callable[[], T_Result]) -> T_Result:
        if self is TrustedKeyResponseDtoAudience.HUMAN:
            return human()
        if self is TrustedKeyResponseDtoAudience.CLIENT:
            return client()
