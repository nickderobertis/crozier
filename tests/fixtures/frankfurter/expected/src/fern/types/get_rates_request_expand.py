

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRatesRequestExpand(enum.StrEnum):
    PROVIDERS = "providers"

    def visit(self, providers: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRatesRequestExpand.PROVIDERS:
            return providers()
