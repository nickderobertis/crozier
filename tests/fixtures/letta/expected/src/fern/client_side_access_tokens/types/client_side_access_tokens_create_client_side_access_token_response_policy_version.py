

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyVersion(enum.StrEnum):
    ONE = "1"

    def visit(self, one: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyVersion.ONE:
            return one()
