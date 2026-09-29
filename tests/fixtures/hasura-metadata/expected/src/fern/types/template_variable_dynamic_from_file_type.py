

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TemplateVariableDynamicFromFileType(enum.StrEnum):
    DYNAMIC_FROM_FILE = "dynamic_from_file"

    def visit(self, dynamic_from_file: typing.Callable[[], T_Result]) -> T_Result:
        if self is TemplateVariableDynamicFromFileType.DYNAMIC_FROM_FILE:
            return dynamic_from_file()
