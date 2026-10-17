

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdatePostgresConfigBodySessionReplicationRole(enum.StrEnum):
    ORIGIN = "origin"
    REPLICA = "replica"
    LOCAL = "local"

    def visit(
        self,
        origin: typing.Callable[[], T_Result],
        replica: typing.Callable[[], T_Result],
        local: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdatePostgresConfigBodySessionReplicationRole.ORIGIN:
            return origin()
        if self is UpdatePostgresConfigBodySessionReplicationRole.REPLICA:
            return replica()
        if self is UpdatePostgresConfigBodySessionReplicationRole.LOCAL:
            return local()
