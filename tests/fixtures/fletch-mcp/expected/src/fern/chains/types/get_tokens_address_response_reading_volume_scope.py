

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensAddressResponseReadingVolumeScope(enum.StrEnum):
    SELECTED_POOL = "selected_pool"

    def visit(self, selected_pool: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTokensAddressResponseReadingVolumeScope.SELECTED_POOL:
            return selected_pool()
