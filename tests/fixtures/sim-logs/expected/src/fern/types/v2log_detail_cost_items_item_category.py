

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2LogDetailCostItemsItemCategory(enum.StrEnum):
    """
    What the line is for: the run's base fee (`fixed`), one model's inference (`model`), or one metered tool or integration call (`tool`).
    """

    FIXED = "fixed"
    MODEL = "model"
    TOOL = "tool"

    def visit(
        self,
        fixed: typing.Callable[[], T_Result],
        model: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2LogDetailCostItemsItemCategory.FIXED:
            return fixed()
        if self is V2LogDetailCostItemsItemCategory.MODEL:
            return model()
        if self is V2LogDetailCostItemsItemCategory.TOOL:
            return tool()
