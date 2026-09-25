

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchModelIdPostprocessConfigBestNPagesOutputFormat(enum.StrEnum):
    V1 = "v1"
    V2 = "v2"

    def visit(self, v1: typing.Callable[[], T_Result], v2: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchModelIdPostprocessConfigBestNPagesOutputFormat.V1:
            return v1()
        if self is PatchModelIdPostprocessConfigBestNPagesOutputFormat.V2:
            return v2()
