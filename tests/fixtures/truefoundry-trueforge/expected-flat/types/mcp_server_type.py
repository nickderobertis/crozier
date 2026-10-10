

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpServerType(enum.StrEnum):
    REMOTE = "remote"
    TRUEFOUNDRY = "truefoundry"

    def visit(self, remote: typing.Callable[[], T_Result], truefoundry: typing.Callable[[], T_Result]) -> T_Result:
        if self is McpServerType.REMOTE:
            return remote()
        if self is McpServerType.TRUEFOUNDRY:
            return truefoundry()
