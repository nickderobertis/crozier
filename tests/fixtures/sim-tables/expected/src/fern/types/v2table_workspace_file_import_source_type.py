

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableWorkspaceFileImportSourceType(enum.StrEnum):
    """
    Workspace-file source discriminator.
    """

    WORKSPACE_FILE = "workspace_file"

    def visit(self, workspace_file: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2TableWorkspaceFileImportSourceType.WORKSPACE_FILE:
            return workspace_file()
