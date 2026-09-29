

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FleetUiMessageChunkStart(UniversalBaseModel):
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")]
    message_metadata: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="messageMetadata"), pydantic.Field(alias="messageMetadata")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
