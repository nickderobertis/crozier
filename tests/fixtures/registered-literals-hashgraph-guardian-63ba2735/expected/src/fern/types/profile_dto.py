

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProfileDto(UniversalBaseModel):
    username: str
    role: str
    did: typing.Optional[str] = None
    parent: typing.Optional[str] = None
    hedera_account_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hederaAccountId"), pydantic.Field(alias="hederaAccountId")
    ] = None
    confirmed: typing.Optional[bool] = None
    failed: typing.Optional[bool] = None
    topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")
    ] = None
    parent_topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentTopicId"), pydantic.Field(alias="parentTopicId")
    ] = None
    did_document: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="didDocument"),
        pydantic.Field(alias="didDocument"),
    ] = None
    vc_document: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="vcDocument"),
        pydantic.Field(alias="vcDocument"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
