

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason(enum.StrEnum):
    PLATFORM_UNSUPPORTED = "platform_unsupported"
    POSTGRES_UPGRADE_REQUIRED = "postgres_upgrade_required"
    SSL_ENFORCEMENT_REQUIRED = "ssl_enforcement_required"
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"

    def visit(
        self,
        platform_unsupported: typing.Callable[[], T_Result],
        postgres_upgrade_required: typing.Callable[[], T_Result],
        ssl_enforcement_required: typing.Callable[[], T_Result],
        temporarily_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason.PLATFORM_UNSUPPORTED:
            return platform_unsupported()
        if self is V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason.POSTGRES_UPGRADE_REQUIRED:
            return postgres_upgrade_required()
        if self is V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason.SSL_ENFORCEMENT_REQUIRED:
            return ssl_enforcement_required()
        if self is V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason.TEMPORARILY_UNAVAILABLE:
            return temporarily_unavailable()
