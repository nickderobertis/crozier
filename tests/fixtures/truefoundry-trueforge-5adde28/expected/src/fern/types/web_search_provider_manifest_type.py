

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebSearchProviderManifestType(enum.StrEnum):
    """
    Parallel web-search provider.
    """

    PARALLEL = "parallel"

    def visit(self, parallel: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebSearchProviderManifestType.PARALLEL:
            return parallel()
