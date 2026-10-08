

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cell_id import CellId
from .code_completion_command_type import CodeCompletionCommandType
from .request_id import RequestId


class CodeCompletionCommand(UniversalBaseModel):
    """
    Request code completion suggestions.

        Sent when the user requests autocomplete. Provides code context up to
        the cursor position for the language server.

        Attributes:
            id: Unique identifier for this request.
            document: Source code up to the cursor position.
            cell_id: Cell where completion is requested.
    """

    cell_id: typing_extensions.Annotated[CellId, FieldMetadata(alias="cellId"), pydantic.Field(alias="cellId")]
    document: str
    id: RequestId
    type: CodeCompletionCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
