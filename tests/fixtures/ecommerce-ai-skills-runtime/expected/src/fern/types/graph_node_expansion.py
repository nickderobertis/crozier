

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GraphNodeExpansion(enum.StrEnum):
    SINGLETON = "singleton"
    EACH_INPUT_MARKETPLACE = "each_input_marketplace"
    MULTIPLE_MARKETPLACES = "multiple_marketplaces"

    def visit(
        self,
        singleton: typing.Callable[[], T_Result],
        each_input_marketplace: typing.Callable[[], T_Result],
        multiple_marketplaces: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GraphNodeExpansion.SINGLETON:
            return singleton()
        if self is GraphNodeExpansion.EACH_INPUT_MARKETPLACE:
            return each_input_marketplace()
        if self is GraphNodeExpansion.MULTIPLE_MARKETPLACES:
            return multiple_marketplaces()
