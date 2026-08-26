

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .model_update_message_buffer_paths_item_item import ModelUpdateMessageBufferPathsItemItem
from .model_update_message_method import ModelUpdateMessageMethod


class ModelUpdateMessage(UniversalBaseModel):
    """
    Widget model state update message.

        Attributes:
            state: Model state updates.
            buffer_paths: Paths within state dict pointing to binary buffers.
    """

    buffer_paths: typing_extensions.Annotated[
        typing.List[typing.List[ModelUpdateMessageBufferPathsItemItem]],
        FieldMetadata(alias="bufferPaths"),
        pydantic.Field(alias="bufferPaths"),
    ]
    method: ModelUpdateMessageMethod
    state: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
