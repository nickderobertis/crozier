

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensAddressResponseSource(enum.StrEnum):
    REGISTRY = "registry"
    DISCOVERED = "discovered"
    NONE = "none"

    def visit(
        self,
        registry: typing.Callable[[], T_Result],
        discovered: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTokensAddressResponseSource.REGISTRY:
            return registry()
        if self is GetTokensAddressResponseSource.DISCOVERED:
            return discovered()
        if self is GetTokensAddressResponseSource.NONE:
            return none()
