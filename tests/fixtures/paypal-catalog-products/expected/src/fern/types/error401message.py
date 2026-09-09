

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error401Message(enum.StrEnum):
    AUTHENTICATION_FAILED_DUE_TO_MISSING_AUTHORIZATION_HEADER_OR_INVALID_AUTHENTICATION_CREDENTIALS = (
        "Authentication failed due to missing authorization header, or invalid authentication credentials."
    )

    def visit(
        self,
        authentication_failed_due_to_missing_authorization_header_or_invalid_authentication_credentials: typing.Callable[
            [], T_Result
        ],
    ) -> T_Result:
        if (
            self
            is Error401Message.AUTHENTICATION_FAILED_DUE_TO_MISSING_AUTHORIZATION_HEADER_OR_INVALID_AUTHENTICATION_CREDENTIALS
        ):
            return authentication_failed_due_to_missing_authorization_header_or_invalid_authentication_credentials()
