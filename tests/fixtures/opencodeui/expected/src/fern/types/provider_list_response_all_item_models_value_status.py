

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderListResponseAllItemModelsValueStatus(enum.StrEnum):
    ALPHA = "alpha"
    BETA = "beta"
    DEPRECATED = "deprecated"

    def visit(
        self,
        alpha: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderListResponseAllItemModelsValueStatus.ALPHA:
            return alpha()
        if self is ProviderListResponseAllItemModelsValueStatus.BETA:
            return beta()
        if self is ProviderListResponseAllItemModelsValueStatus.DEPRECATED:
            return deprecated()
