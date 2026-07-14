

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AttemptFailureType(str, enum.Enum):
    """
    Categorizes well known errors into types for programmatic handling. If not set, the type of error is not well known.
    """

    CONFIG_ERROR = "config_error"
    SYSTEM_ERROR = "system_error"
    MANUAL_CANCELLATION = "manual_cancellation"
    REFRESH_SCHEMA = "refresh_schema"

    def visit(
        self,
        config_error: typing.Callable[[], T_Result],
        system_error: typing.Callable[[], T_Result],
        manual_cancellation: typing.Callable[[], T_Result],
        refresh_schema: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AttemptFailureType.CONFIG_ERROR:
            return config_error()
        if self is AttemptFailureType.SYSTEM_ERROR:
            return system_error()
        if self is AttemptFailureType.MANUAL_CANCELLATION:
            return manual_cancellation()
        if self is AttemptFailureType.REFRESH_SCHEMA:
            return refresh_schema()
