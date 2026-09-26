

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderAuthMethodTypeOne(enum.StrEnum):
    API = "api"

    def visit(self, api: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProviderAuthMethodTypeOne.API:
            return api()
