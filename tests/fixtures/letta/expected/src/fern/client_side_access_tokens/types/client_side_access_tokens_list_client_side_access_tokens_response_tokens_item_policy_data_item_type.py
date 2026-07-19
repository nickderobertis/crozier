

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemType(enum.StrEnum):
    AGENT = "agent"

    def visit(self, agent: typing.Callable[[], T_Result]) -> T_Result:
        if self is ClientSideAccessTokensListClientSideAccessTokensResponseTokensItemPolicyDataItemType.AGENT:
            return agent()
