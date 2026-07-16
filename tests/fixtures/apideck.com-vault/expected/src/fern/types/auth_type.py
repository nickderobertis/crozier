

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthType(enum.StrEnum):
    """
    Type of authorization used by the connector
    """

    OAUTH2 = "oauth2"
    API_KEY = "apiKey"
    BASIC = "basic"
    CUSTOM = "custom"
    NONE = "none"

    def visit(
        self,
        oauth2: typing.Callable[[], T_Result],
        api_key: typing.Callable[[], T_Result],
        basic: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthType.OAUTH2:
            return oauth2()
        if self is AuthType.API_KEY:
            return api_key()
        if self is AuthType.BASIC:
            return basic()
        if self is AuthType.CUSTOM:
            return custom()
        if self is AuthType.NONE:
            return none()
