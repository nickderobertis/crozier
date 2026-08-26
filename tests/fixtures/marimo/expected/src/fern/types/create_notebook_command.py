

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_notebook_command_type import CreateNotebookCommandType
from .execute_cell_command import ExecuteCellCommand
from .http_request import HttpRequest
from .update_ui_element_command import UpdateUiElementCommand


class CreateNotebookCommand(UniversalBaseModel):
    """
    Instantiate and initialize a notebook.

        Sent when a notebook is first loaded. Contains all cells and initial UI element values.

        Attributes:
            execution_requests: ExecuteCellCommand for each notebook cell.
            cell_ids: Initial cell IDs in the notebook.
            set_ui_element_value_request: Initial UI element values.
            auto_run: Whether to automatically execute cells on instantiation.
            request: HTTP request context if available.
    """

    auto_run: typing_extensions.Annotated[bool, FieldMetadata(alias="autoRun"), pydantic.Field(alias="autoRun")]
    cell_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="cellIds"), pydantic.Field(alias="cellIds")
    ]
    execution_requests: typing_extensions.Annotated[
        typing.List[ExecuteCellCommand],
        FieldMetadata(alias="executionRequests"),
        pydantic.Field(alias="executionRequests"),
    ]
    request: typing.Optional[HttpRequest] = None
    set_ui_element_value_request: typing_extensions.Annotated[
        UpdateUiElementCommand,
        FieldMetadata(alias="setUiElementValueRequest"),
        pydantic.Field(alias="setUiElementValueRequest"),
    ]
    type: CreateNotebookCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
