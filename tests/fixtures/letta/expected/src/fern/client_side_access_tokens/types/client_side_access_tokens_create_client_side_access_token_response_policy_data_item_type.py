

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemType(enum.StrEnum):
    AGENT = "agent"

    def visit(self, agent: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClientSideAccessTokensCreateClientSideAccessTokenResponsePolicyDataItemType.AGENT:
            return agent()
