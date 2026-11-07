

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MultiPartyAuthorizeRequestAuthorizationType(enum.StrEnum):
    MULTI_PARTY_AUTHORIZATION = "multi_party_authorization"

    def visit(self, multi_party_authorization: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultiPartyAuthorizeRequestAuthorizationType.MULTI_PARTY_AUTHORIZATION:
            return multi_party_authorization()
