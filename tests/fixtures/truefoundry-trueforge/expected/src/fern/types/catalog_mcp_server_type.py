

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogMcpServerType(enum.StrEnum):
    REMOTE = "remote"

    def visit(self, remote: typing.Callable[[], T_Result]) -> T_Result:
        if self is CatalogMcpServerType.REMOTE:
            return remote()
