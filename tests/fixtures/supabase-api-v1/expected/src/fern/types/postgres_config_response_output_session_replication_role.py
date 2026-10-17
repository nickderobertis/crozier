

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostgresConfigResponseOutputSessionReplicationRole(enum.StrEnum):
    ORIGIN = "origin"
    REPLICA = "replica"
    LOCAL = "local"

    def visit(
        self,
        origin: typing.Callable[[], T_Result],
        replica: typing.Callable[[], T_Result],
        local: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostgresConfigResponseOutputSessionReplicationRole.ORIGIN:
            return origin()
        if self is PostgresConfigResponseOutputSessionReplicationRole.REPLICA:
            return replica()
        if self is PostgresConfigResponseOutputSessionReplicationRole.LOCAL:
            return local()
