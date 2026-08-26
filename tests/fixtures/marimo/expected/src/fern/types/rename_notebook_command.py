

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rename_notebook_command_type import RenameNotebookCommandType


class RenameNotebookCommand(UniversalBaseModel):
    """
    Rename or move the notebook file.

        Updates the notebook's filename in the kernel metadata.

        Attributes:
            filename: New filename or path for the notebook.
    """

    filename: str
    type: RenameNotebookCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
