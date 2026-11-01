

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchPageRequestCoverType(enum.StrEnum):
    EXTERNAL = "external"

    def visit(self, external: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchPageRequestCoverType.EXTERNAL:
            return external()
