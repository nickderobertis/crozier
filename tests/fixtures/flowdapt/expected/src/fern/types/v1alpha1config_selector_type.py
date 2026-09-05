

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1Alpha1ConfigSelectorType(enum.StrEnum):
    NAME = "name"
    ANNOTATION = "annotation"

    def visit(self, name: typing.Callable[[], T_Result], annotation: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1Alpha1ConfigSelectorType.NAME:
            return name()
        if self is V1Alpha1ConfigSelectorType.ANNOTATION:
            return annotation()
