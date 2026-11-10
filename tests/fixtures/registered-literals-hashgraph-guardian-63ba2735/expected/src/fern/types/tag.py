

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tag_entity import TagEntity
from .tag_operation import TagOperation
from .tag_status import TagStatus


class Tag(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    name: str
    description: typing.Optional[str] = None
    owner: typing.Optional[str] = None
    entity: TagEntity
    target: typing.Optional[str] = None
    local_target: typing_extensions.Annotated[
        str, FieldMetadata(alias="localTarget"), pydantic.Field(alias="localTarget")
    ]
    status: typing.Optional[TagStatus] = None
    operation: typing.Optional[TagOperation] = None
    date: typing.Optional[str] = None
    topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")
    ] = None
    message_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")
    ] = None
    policy_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="policyId"), pydantic.Field(alias="policyId")
    ] = None
    uri: typing.Optional[str] = None
    document: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
