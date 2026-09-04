

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType(enum.StrEnum):
    """
    The response type for the user info endpoint should be configurable to allow the Relying Party to choose between only signed tokens or signed tokens with encryption.
    """

    JWS = "JWS"
    JWE = "JWE"

    def visit(self, jws: typing.Callable[[], T_Result], jwe: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType.JWS:
            return jws()
        if self is PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType.JWE:
            return jwe()
