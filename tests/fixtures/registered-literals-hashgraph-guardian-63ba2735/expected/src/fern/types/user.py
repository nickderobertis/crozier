

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class User(UniversalBaseModel):
    confirmed: typing.Optional[str] = None
    failed: typing.Optional[str] = None
    username: str
    role: str
    hedera_account_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hederaAccountId"), pydantic.Field(alias="hederaAccountId")
    ] = None
    hedera_account_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hederaAccountKey"), pydantic.Field(alias="hederaAccountKey")
    ] = None
    did: typing.Optional[str] = None
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
    parent: typing.Optional[str] = None
    topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
