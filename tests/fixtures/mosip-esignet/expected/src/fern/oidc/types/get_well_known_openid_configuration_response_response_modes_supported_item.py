

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem(enum.StrEnum):
    QUERY = "query"

    def visit(self, query: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem.QUERY:
            return query()
