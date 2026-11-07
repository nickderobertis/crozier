

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EdgeMessageHeader(UniversalBaseModel):
    subject: str
    content_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ]
    content_length: typing_extensions.Annotated[
        int, FieldMetadata(alias="contentLength"), pydantic.Field(alias="contentLength")
    ]
    content_encoding: typing_extensions.Annotated[
        str, FieldMetadata(alias="contentEncoding"), pydantic.Field(alias="contentEncoding")
    ]
    message_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    recipient: typing.Optional[str] = None
    reply_to: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="replyTo"), pydantic.Field(alias="replyTo")
    ] = None
    correlation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="correlationId"), pydantic.Field(alias="correlationId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
