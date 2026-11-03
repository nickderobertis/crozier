

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListParcelsRequestLabelStyle(enum.StrEnum):
    PLAIN = "plain"
    BOLD = "bold"

    def visit(self, plain: typing.Callable[[], T_Result], bold: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListParcelsRequestLabelStyle.PLAIN:
            return plain()
        if self is ListParcelsRequestLabelStyle.BOLD:
            return bold()
