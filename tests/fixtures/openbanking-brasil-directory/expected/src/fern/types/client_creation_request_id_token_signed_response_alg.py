

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ClientCreationRequestIdTokenSignedResponseAlg(enum.StrEnum):
    """
    Signing algorithim that a client expects the server to return an id_token with. Must be PS256
    """

    PS256 = "PS256"

    def visit(self, ps256: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClientCreationRequestIdTokenSignedResponseAlg.PS256:
            return ps256()
