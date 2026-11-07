

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCurrentJwtKeyPairRequestAudience(enum.StrEnum):
    HUMAN = "human"
    CLIENT = "client"

    def visit(self, human: typing.Callable[[], T_Result], client: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCurrentJwtKeyPairRequestAudience.HUMAN:
            return human()
        if self is GetCurrentJwtKeyPairRequestAudience.CLIENT:
            return client()
