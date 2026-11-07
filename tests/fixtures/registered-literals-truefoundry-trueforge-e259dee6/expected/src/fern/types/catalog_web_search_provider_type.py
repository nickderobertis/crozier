

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogWebSearchProviderType(enum.StrEnum):
    """
    Parallel web-search provider.
    """

    PARALLEL = "parallel"

    def visit(self, parallel: typing.Callable[[], T_Result]) -> T_Result:
        if self is CatalogWebSearchProviderType.PARALLEL:
            return parallel()
