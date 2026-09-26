

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderConfigModelsValueStatus(enum.StrEnum):
    ALPHA = "alpha"
    BETA = "beta"
    DEPRECATED = "deprecated"

    def visit(
        self,
        alpha: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderConfigModelsValueStatus.ALPHA:
            return alpha()
        if self is ProviderConfigModelsValueStatus.BETA:
            return beta()
        if self is ProviderConfigModelsValueStatus.DEPRECATED:
            return deprecated()
