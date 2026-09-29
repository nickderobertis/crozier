

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FleetUiMessageChunkDataAttachmentData(UniversalBaseModel):
    attachment_id: str
    filename: str
    phase: typing.Optional[str] = None
    byte_size: typing.Optional[int] = None
    attachment_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="attachmentId"), pydantic.Field(alias="attachmentId")
    ] = None
    byte_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="byteSize"), pydantic.Field(alias="byteSize")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
