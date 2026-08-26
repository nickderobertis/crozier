

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sync_graph_command_type import SyncGraphCommandType


class SyncGraphCommand(UniversalBaseModel):
    """
    Synchronize the kernel graph with file manager state.

        Used when the notebook file changes externally (e.g., file reload or version control).
        Updates changed cells, deletes removed cells, and optionally executes modified cells.

        Attributes:
            cells: All cells known to file manager, mapping cell_id to code.
            run_ids: Cells to execute or update.
            delete_ids: Cells to delete from the graph.
            timestamp: Unix timestamp when command was created.
    """

    cells: typing.Dict[str, str]
    delete_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="deleteIds"), pydantic.Field(alias="deleteIds")
    ]
    run_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="runIds"), pydantic.Field(alias="runIds")
    ]
    timestamp: typing.Optional[float] = None
    type: SyncGraphCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
