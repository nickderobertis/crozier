

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fleet_ui_message_chunk_finish_finish_reason import FleetUiMessageChunkFinishFinishReason


class FleetUiMessageChunkFinish(UniversalBaseModel):
    finish_reason: typing_extensions.Annotated[
        FleetUiMessageChunkFinishFinishReason, FieldMetadata(alias="finishReason"), pydantic.Field(alias="finishReason")
    ]
    message_metadata: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="messageMetadata"),
        pydantic.Field(alias="messageMetadata"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
