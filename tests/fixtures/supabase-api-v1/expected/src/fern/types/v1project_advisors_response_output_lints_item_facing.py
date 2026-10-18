

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectAdvisorsResponseOutputLintsItemFacing(enum.StrEnum):
    EXTERNAL = "EXTERNAL"

    def visit(self, external: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ProjectAdvisorsResponseOutputLintsItemFacing.EXTERNAL:
            return external()
