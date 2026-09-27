

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchResultTitleStatus(enum.StrEnum):
    """
    Present for title hits; manual titles must always be displayed verbatim.
    """

    AUTO_PENDING = "auto_pending"
    AUTO = "auto"
    MANUAL = "manual"

    def visit(
        self,
        auto_pending: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchResultTitleStatus.AUTO_PENDING:
            return auto_pending()
        if self is SearchResultTitleStatus.AUTO:
            return auto()
        if self is SearchResultTitleStatus.MANUAL:
            return manual()
