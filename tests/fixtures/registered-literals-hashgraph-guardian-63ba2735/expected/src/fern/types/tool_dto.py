

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ToolDto(UniversalBaseModel):
    id: str
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    name: str
    description: str
    config: typing.Dict[str, typing.Any]
    status: str
    creator: str
    owner: str
    topic_id: typing_extensions.Annotated[str, FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")]
    code_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="codeVersion"), pydantic.Field(alias="codeVersion")
    ]
    create_date: typing_extensions.Annotated[str, FieldMetadata(alias="createDate"), pydantic.Field(alias="createDate")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
