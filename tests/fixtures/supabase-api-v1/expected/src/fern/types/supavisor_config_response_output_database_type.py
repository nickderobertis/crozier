

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SupavisorConfigResponseOutputDatabaseType(enum.StrEnum):
    PRIMARY = "PRIMARY"
    READ_REPLICA = "READ_REPLICA"

    def visit(self, primary: typing.Callable[[], T_Result], read_replica: typing.Callable[[], T_Result]) -> T_Result:
        if self is SupavisorConfigResponseOutputDatabaseType.PRIMARY:
            return primary()
        if self is SupavisorConfigResponseOutputDatabaseType.READ_REPLICA:
            return read_replica()
