

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .delete_cell_command_type import DeleteCellCommandType


class DeleteCellCommand(UniversalBaseModel):
    """
    Delete a cell from the notebook.

        Removes cell from the dependency graph and cleans up its variables.
        Dependent cells may become stale.

        Attributes:
            cell_id: Cell to delete.
    """

    cell_id: typing_extensions.Annotated[CellId, FieldMetadata(alias="cellId"), pydantic.Field(alias="cellId")]
    type: DeleteCellCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
