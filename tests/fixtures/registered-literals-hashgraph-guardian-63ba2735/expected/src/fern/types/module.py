

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Module(UniversalBaseModel):
    id: typing.Optional[str] = None
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    config: typing.Optional[typing.Dict[str, typing.Any]] = None
    status: typing.Optional[str] = None
    creator: typing.Optional[str] = None
    owner: typing.Optional[str] = None
    topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")
    ] = None
    message_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")
    ] = None
    code_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="codeVersion"), pydantic.Field(alias="codeVersion")
    ] = None
    create_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createDate"), pydantic.Field(alias="createDate")
    ] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
