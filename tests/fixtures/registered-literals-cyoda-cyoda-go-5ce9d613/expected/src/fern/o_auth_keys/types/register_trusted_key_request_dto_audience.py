

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RegisterTrustedKeyRequestDtoAudience(enum.StrEnum):
    HUMAN = "human"
    CLIENT = "client"

    def visit(self, human: typing.Callable[[], T_Result], client: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegisterTrustedKeyRequestDtoAudience.HUMAN:
            return human()
        if self is RegisterTrustedKeyRequestDtoAudience.CLIENT:
            return client()
