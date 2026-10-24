

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarketplaceAccountHealthErrorCode(enum.StrEnum):
    MISSING_CREDENTIAL = "missing_credential"
    INVALID_CONFIGURATION = "invalid_configuration"
    RATE_LIMITED = "rate_limited"
    EXTERNAL_SERVICE_ERROR = "external_service_error"

    def visit(
        self,
        missing_credential: typing.Callable[[], T_Result],
        invalid_configuration: typing.Callable[[], T_Result],
        rate_limited: typing.Callable[[], T_Result],
        external_service_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarketplaceAccountHealthErrorCode.MISSING_CREDENTIAL:
            return missing_credential()
        if self is MarketplaceAccountHealthErrorCode.INVALID_CONFIGURATION:
            return invalid_configuration()
        if self is MarketplaceAccountHealthErrorCode.RATE_LIMITED:
            return rate_limited()
        if self is MarketplaceAccountHealthErrorCode.EXTERNAL_SERVICE_ERROR:
            return external_service_error()
