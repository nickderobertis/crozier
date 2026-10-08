

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateNotebookCommandType(enum.StrEnum):
    CREATE_NOTEBOOK = "create-notebook"

    def visit(self, create_notebook: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateNotebookCommandType.CREATE_NOTEBOOK:
            return create_notebook()
