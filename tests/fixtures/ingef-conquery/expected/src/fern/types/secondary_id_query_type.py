

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SecondaryIdQueryType(enum.StrEnum):
    SECONDARY_ID_QUERY = "SECONDARY_ID_QUERY"

    def visit(self, secondary_id_query: typing.Callable[[], T_Result]) -> T_Result:
        if self is SecondaryIdQueryType.SECONDARY_ID_QUERY:
            return secondary_id_query()
