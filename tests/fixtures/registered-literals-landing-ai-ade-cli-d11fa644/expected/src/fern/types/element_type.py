

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ElementType(enum.StrEnum):
    """
    The element type. Determines which optional fields appear on this element.
    """

    TEXT = "text"
    TABLE = "table"
    TABLE_CELL = "table_cell"
    FIGURE = "figure"
    MARGINALIA = "marginalia"
    ATTESTATION = "attestation"
    LOGO = "logo"
    CARD = "card"
    SCAN_CODE = "scan_code"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        table: typing.Callable[[], T_Result],
        table_cell: typing.Callable[[], T_Result],
        figure: typing.Callable[[], T_Result],
        marginalia: typing.Callable[[], T_Result],
        attestation: typing.Callable[[], T_Result],
        logo: typing.Callable[[], T_Result],
        card: typing.Callable[[], T_Result],
        scan_code: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ElementType.TEXT:
            return text()
        if self is ElementType.TABLE:
            return table()
        if self is ElementType.TABLE_CELL:
            return table_cell()
        if self is ElementType.FIGURE:
            return figure()
        if self is ElementType.MARGINALIA:
            return marginalia()
        if self is ElementType.ATTESTATION:
            return attestation()
        if self is ElementType.LOGO:
            return logo()
        if self is ElementType.CARD:
            return card()
        if self is ElementType.SCAN_CODE:
            return scan_code()
