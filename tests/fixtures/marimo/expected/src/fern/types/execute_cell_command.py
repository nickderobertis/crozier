

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .execute_cell_command_type import ExecuteCellCommandType
from .http_request import HttpRequest


class ExecuteCellCommand(UniversalBaseModel):
    """
    Execute a single cell.

        Executes a cell with the provided code. Dependent cells may be
        re-executed based on the reactive execution mode.

        Attributes:
            cell_id: Cell to execute.
            code: Python code to execute.
            request: HTTP request context if available.
            timestamp: Unix timestamp when command was created.
    """

    cell_id: typing_extensions.Annotated[CellId, FieldMetadata(alias="cellId"), pydantic.Field(alias="cellId")]
    code: str
    request: typing.Optional[HttpRequest] = None
    timestamp: typing.Optional[float] = None
    type: ExecuteCellCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
