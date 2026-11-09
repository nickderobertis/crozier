

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationMetadataDirectoryServer(enum.StrEnum):
    AMERICAN_EXPRESS = "american_express"
    MASTERCARD = "mastercard"
    VISA = "visa"

    def visit(
        self,
        american_express: typing.Callable[[], T_Result],
        mastercard: typing.Callable[[], T_Result],
        visa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationMetadataDirectoryServer.AMERICAN_EXPRESS:
            return american_express()
        if self is AuthenticationMetadataDirectoryServer.MASTERCARD:
            return mastercard()
        if self is AuthenticationMetadataDirectoryServer.VISA:
            return visa()
