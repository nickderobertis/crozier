

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntitySchemaBaseAuthParentOption(enum.StrEnum):
    FOLDER = "FOLDER"
    PROJECT_FOLDER = "PROJECT_FOLDER"

    def visit(self, folder: typing.Callable[[], T_Result], project_folder: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntitySchemaBaseAuthParentOption.FOLDER:
            return folder()
        if self is EntitySchemaBaseAuthParentOption.PROJECT_FOLDER:
            return project_folder()
