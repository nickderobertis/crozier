

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ClientUpdateRequestIdTokenSignedResponseAlg(enum.StrEnum):
    """
    Signing algorithim that a client expects the server to return an id_token with. Must be PS256
    """

    PS256 = "PS256"

    def visit(self, ps256: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClientUpdateRequestIdTokenSignedResponseAlg.PS256:
            return ps256()
