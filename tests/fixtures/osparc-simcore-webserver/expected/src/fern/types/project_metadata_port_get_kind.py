

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectMetadataPortGetKind(enum.StrEnum):
    INPUT = "input"
    OUTPUT = "output"

    def visit(self, input: typing.Callable[[], T_Result], output: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectMetadataPortGetKind.INPUT:
            return input()
        if self is ProjectMetadataPortGetKind.OUTPUT:
            return output()
