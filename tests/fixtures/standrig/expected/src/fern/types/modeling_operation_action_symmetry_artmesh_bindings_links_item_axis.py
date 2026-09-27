

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionSymmetryArtmeshBindingsLinksItemAxis(enum.StrEnum):
    X = "x"

    def visit(self, x: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionSymmetryArtmeshBindingsLinksItemAxis.X:
            return x()
