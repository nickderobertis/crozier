

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAccessTokenRequestGrantType(enum.StrEnum):
    CLIENT_CREDENTIALS = "client_credentials"

    def visit(self, client_credentials: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAccessTokenRequestGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
