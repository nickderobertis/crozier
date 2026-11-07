

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowImportRequestDtoImportMode(enum.StrEnum):
    """
    Import mode for handling existing workflows
    """

    REPLACE = "REPLACE"
    ACTIVATE = "ACTIVATE"
    MERGE = "MERGE"

    def visit(
        self,
        replace: typing.Callable[[], T_Result],
        activate: typing.Callable[[], T_Result],
        merge: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowImportRequestDtoImportMode.REPLACE:
            return replace()
        if self is WorkflowImportRequestDtoImportMode.ACTIVATE:
            return activate()
        if self is WorkflowImportRequestDtoImportMode.MERGE:
            return merge()
