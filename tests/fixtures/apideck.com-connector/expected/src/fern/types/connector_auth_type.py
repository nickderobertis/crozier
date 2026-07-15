

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectorAuthType(str, enum.Enum):
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
        if self is ConnectorAuthType.OAUTH2:
            return oauth2()
        if self is ConnectorAuthType.API_KEY:
            return api_key()
        if self is ConnectorAuthType.BASIC:
            return basic()
        if self is ConnectorAuthType.CUSTOM:
            return custom()
        if self is ConnectorAuthType.NONE:
            return none()
