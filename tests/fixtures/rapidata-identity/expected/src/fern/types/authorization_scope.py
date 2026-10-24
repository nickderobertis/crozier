

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorizationScope(enum.StrEnum):
    PLATFORM = "Platform"
    BIDDER = "Bidder"
    EXTERNAL_APP = "ExternalApp"

    def visit(
        self,
        platform: typing.Callable[[], T_Result],
        bidder: typing.Callable[[], T_Result],
        external_app: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthorizationScope.PLATFORM:
            return platform()
        if self is AuthorizationScope.BIDDER:
            return bidder()
        if self is AuthorizationScope.EXTERNAL_APP:
            return external_app()
