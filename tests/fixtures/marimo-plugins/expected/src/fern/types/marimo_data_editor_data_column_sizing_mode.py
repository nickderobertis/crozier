

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoDataEditorDataColumnSizingMode(enum.StrEnum):
    AUTO = "auto"
    FIT = "fit"

    def visit(self, auto: typing.Callable[[], T_Result], fit: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoDataEditorDataColumnSizingMode.AUTO:
            return auto()
        if self is MarimoDataEditorDataColumnSizingMode.FIT:
            return fit()
