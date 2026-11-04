

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxEnvironmentImageType(enum.StrEnum):
    """
    Build a snapshot from a script.
    """

    BUILD = "build"

    def visit(self, build: typing.Callable[[], T_Result]) -> T_Result:
        if self is SandboxEnvironmentImageType.BUILD:
            return build()
