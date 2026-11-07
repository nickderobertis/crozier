

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class IssueJwtKeyPairRequestDtoAudience(enum.StrEnum):
    HUMAN = "human"
    CLIENT = "client"

    def visit(self, human: typing.Callable[[], T_Result], client: typing.Callable[[], T_Result]) -> T_Result:
        if self is IssueJwtKeyPairRequestDtoAudience.HUMAN:
            return human()
        if self is IssueJwtKeyPairRequestDtoAudience.CLIENT:
            return client()
