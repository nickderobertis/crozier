

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionCitationGranularity(enum.StrEnum):
    """
    Citation geometry granularity. Citation v1 emits `element` and `table_cell`;
    `text_span` is reserved for a later narrowing release.
    """

    ELEMENT = "element"
    TABLE_CELL = "table_cell"
    TEXT_SPAN = "text_span"

    def visit(
        self,
        element: typing.Callable[[], T_Result],
        table_cell: typing.Callable[[], T_Result],
        text_span: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExtractionCitationGranularity.ELEMENT:
            return element()
        if self is ExtractionCitationGranularity.TABLE_CELL:
            return table_cell()
        if self is ExtractionCitationGranularity.TEXT_SPAN:
            return text_span()
