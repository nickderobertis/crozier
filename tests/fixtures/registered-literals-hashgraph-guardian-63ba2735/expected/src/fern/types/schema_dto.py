

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SchemaDto(UniversalBaseModel):
    id: str
    name: str
    description: str
    entity: str
    document: str
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    iri: str
    hash: str
    status: str
    topic_id: typing_extensions.Annotated[str, FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")]
    version: str
    owner: str
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
