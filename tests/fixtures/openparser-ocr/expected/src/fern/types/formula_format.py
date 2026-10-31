

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FormulaFormat(enum.StrEnum):
    LATEX = "latex"
    MATHML = "mathml"
    PLAIN = "plain"
    UNKNOWN = "unknown"

    def visit(
        self,
        latex: typing.Callable[[], T_Result],
        mathml: typing.Callable[[], T_Result],
        plain: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FormulaFormat.LATEX:
            return latex()
        if self is FormulaFormat.MATHML:
            return mathml()
        if self is FormulaFormat.PLAIN:
            return plain()
        if self is FormulaFormat.UNKNOWN:
            return unknown()
