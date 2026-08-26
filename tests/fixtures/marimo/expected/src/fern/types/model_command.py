

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .base64string import Base64String
from .model_command_message import ModelCommandMessage
from .model_command_type import ModelCommandType
from .widget_model_id import WidgetModelId


class ModelCommand(UniversalBaseModel):
    """
    Widget model message command.

        Handles widget model communication between frontend and backend.

        Attributes:
            model_id: Widget model identifier.
            message: Model message (update or custom).
            buffers: Base64-encoded binary buffers.
            token: Unique identifier for deduplication across dual queues.
    """

    buffers: typing.List[Base64String]
    message: ModelCommandMessage
    model_id: typing_extensions.Annotated[
        WidgetModelId, FieldMetadata(alias="modelId"), pydantic.Field(alias="modelId")
    ]
    token: typing.Optional[str] = None
    type: ModelCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
