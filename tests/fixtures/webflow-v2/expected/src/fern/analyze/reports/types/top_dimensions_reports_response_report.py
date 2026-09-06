

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopDimensionsReportsResponseReport(enum.StrEnum):
    """
    Discriminator identifying the report type.
    """

    TOP_DIMENSIONS = "top_dimensions"

    def visit(self, top_dimensions: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopDimensionsReportsResponseReport.TOP_DIMENSIONS:
            return top_dimensions()
