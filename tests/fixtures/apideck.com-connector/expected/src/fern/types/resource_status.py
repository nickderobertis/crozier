

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourceStatus(enum.StrEnum):
    """
    Status of the resource. Resources with status live or beta are callable.
    """

    LIVE = "live"
    BETA = "beta"
    DEVELOPMENT = "development"
    UPCOMING = "upcoming"
    CONSIDERING = "considering"

    def visit(
        self,
        live: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        development: typing.Callable[[], T_Result],
        upcoming: typing.Callable[[], T_Result],
        considering: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourceStatus.LIVE:
            return live()
        if self is ResourceStatus.BETA:
            return beta()
        if self is ResourceStatus.DEVELOPMENT:
            return development()
        if self is ResourceStatus.UPCOMING:
            return upcoming()
        if self is ResourceStatus.CONSIDERING:
            return considering()
