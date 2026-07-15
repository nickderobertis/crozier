

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ApiStatus(str, enum.Enum):
    """
    Status of the API. APIs with status live or beta are callable.
    """

    LIVE = "live"
    BETA = "beta"
    DEVELOPMENT = "development"
    CONSIDERING = "considering"

    def visit(
        self,
        live: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        development: typing.Callable[[], T_Result],
        considering: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApiStatus.LIVE:
            return live()
        if self is ApiStatus.BETA:
            return beta()
        if self is ApiStatus.DEVELOPMENT:
            return development()
        if self is ApiStatus.CONSIDERING:
            return considering()
