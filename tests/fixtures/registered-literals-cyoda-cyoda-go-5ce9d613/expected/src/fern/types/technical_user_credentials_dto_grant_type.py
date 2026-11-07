

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TechnicalUserCredentialsDtoGrantType(enum.StrEnum):
    """
    The OAuth2 grant type (must be 'client_credentials')
    """

    CLIENT_CREDENTIALS = "client_credentials"

    def visit(self, client_credentials: typing.Callable[[], T_Result]) -> T_Result:
        if self is TechnicalUserCredentialsDtoGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
