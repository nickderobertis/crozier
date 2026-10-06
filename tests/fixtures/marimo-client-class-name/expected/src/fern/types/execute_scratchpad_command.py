

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_outputs import CellOutputs
from .execute_scratchpad_command_type import ExecuteScratchpadCommandType
from .http_request import HttpRequest
from .notebook_cell import NotebookCell


class ExecuteScratchpadCommand(UniversalBaseModel):
    """
    Execute code in the scratchpad.

        The scratchpad is a temporary execution environment that doesn't affect
        the notebook's cells or dependencies. Runs in an isolated cell with a copy
        of the global namespace, useful for experimentation.

        Attributes:
            code: Python code to execute.
            request: HTTP request context if available.
            notebook_cells: Snapshot of notebook cells from the session document.
                Used to populate the document ContextVar so code_mode can read
                cell ordering, code, names, and configs.
            cell_outputs: Snapshot of per-cell outputs (main + console) from the
                session view. Populates a parallel ContextVar so code_mode can
                expose `cell.output` and `cell.console_outputs`. Frozen at
                scratchpad start — not refreshed when `ctx.run_cell` produces
                new outputs in the same batch.
            run_id: Optional correlation ID. When set, the
                `CompletedRunNotification` emitted at the end of this command
                carries the same `run_id` so a caller holding a
                `ScratchCellListener` can filter for *its* completion and
                ignore `CompletedRun` events from unrelated commands on the
                same session.
    """

    cell_outputs: typing_extensions.Annotated[
        typing.Optional[CellOutputs], FieldMetadata(alias="cellOutputs"), pydantic.Field(alias="cellOutputs")
    ] = None
    code: str
    notebook_cells: typing_extensions.Annotated[
        typing.Optional[typing.List[NotebookCell]],
        FieldMetadata(alias="notebookCells"),
        pydantic.Field(alias="notebookCells"),
    ] = None
    request: typing.Optional[HttpRequest] = None
    run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="runId"), pydantic.Field(alias="runId")
    ] = None
    type: ExecuteScratchpadCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
