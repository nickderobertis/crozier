

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .debug_cell_command_type import DebugCellCommandType
from .http_request import HttpRequest


class DebugCellCommand(UniversalBaseModel):
    """
    Enter debugger mode for a cell.

        Starts the Python debugger (pdb) for the specified cell.

        Attributes:
            cell_id: Cell to debug.
            request: HTTP request context if available.
    """

    cell_id: typing_extensions.Annotated[CellId, FieldMetadata(alias="cellId"), pydantic.Field(alias="cellId")]
    request: typing.Optional[HttpRequest] = None
    type: DebugCellCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
