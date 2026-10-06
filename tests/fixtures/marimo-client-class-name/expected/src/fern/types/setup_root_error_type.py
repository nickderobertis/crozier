

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SetupRootErrorType(enum.StrEnum):
    SETUP_REFS = "setup-refs"

    def visit(self, setup_refs: typing.Callable[[], T_Result]) -> T_Result:
        if self is SetupRootErrorType.SETUP_REFS:
            return setup_refs()
