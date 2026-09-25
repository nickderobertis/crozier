

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardCapabilitiesRemotePreconditioningScopeName(enum.StrEnum):
    REMOTE_PRECONDITIONING_WRITE = "remote:preconditioning:write"

    def visit(self, remote_preconditioning_write: typing.Callable[[], T_Result]) -> T_Result:
        if self is OnboardCapabilitiesRemotePreconditioningScopeName.REMOTE_PRECONDITIONING_WRITE:
            return remote_preconditioning_write()
