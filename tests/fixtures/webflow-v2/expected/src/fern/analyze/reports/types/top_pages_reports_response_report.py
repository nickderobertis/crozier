

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopPagesReportsResponseReport(enum.StrEnum):
    """
    Discriminator identifying the report type.
    """

    TOP_PAGES = "top_pages"

    def visit(self, top_pages: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopPagesReportsResponseReport.TOP_PAGES:
            return top_pages()
