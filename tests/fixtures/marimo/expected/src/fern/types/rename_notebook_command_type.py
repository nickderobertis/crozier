

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RenameNotebookCommandType(enum.StrEnum):
    RENAME_NOTEBOOK = "rename-notebook"

    def visit(self, rename_notebook: typing.Callable[[], T_Result]) -> T_Result:
        if self is RenameNotebookCommandType.RENAME_NOTEBOOK:
            return rename_notebook()
