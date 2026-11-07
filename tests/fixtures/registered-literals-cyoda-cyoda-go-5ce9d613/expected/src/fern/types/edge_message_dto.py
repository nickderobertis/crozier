

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .edge_message_header import EdgeMessageHeader
from .edge_message_meta_data import EdgeMessageMetaData


class EdgeMessageDto(UniversalBaseModel):
    header: EdgeMessageHeader
    meta_data: typing_extensions.Annotated[
        EdgeMessageMetaData, FieldMetadata(alias="metaData"), pydantic.Field(alias="metaData")
    ]
    content: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
