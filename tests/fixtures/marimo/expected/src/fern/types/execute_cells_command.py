

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .execute_cells_command_type import ExecuteCellsCommandType
from .http_request import HttpRequest


class ExecuteCellsCommand(UniversalBaseModel):
    """
    Execute multiple cells in a batch.

        Executes multiple cells with their corresponding code. The kernel manages
        dependency tracking and reactive execution.

        Attributes:
            cell_ids: Cells to execute.
            codes: Python code for each cell. Must match length of cell_ids.
            request: HTTP request context if available.
            timestamp: Unix timestamp when command was created.
    """

    cell_ids: typing_extensions.Annotated[
        typing.List[CellId], FieldMetadata(alias="cellIds"), pydantic.Field(alias="cellIds")
    ]
    codes: typing.List[str]
    request: typing.Optional[HttpRequest] = None
    timestamp: typing.Optional[float] = None
    type: ExecuteCellsCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
