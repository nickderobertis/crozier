

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .review_draft_status import ReviewDraftStatus
from .review_reply_status import ReviewReplyStatus


class Review(UniversalBaseModel):
    id: str
    business_id: typing_extensions.Annotated[str, FieldMetadata(alias="businessId"), pydantic.Field(alias="businessId")]
    platform: str
    external_id: typing_extensions.Annotated[str, FieldMetadata(alias="externalId"), pydantic.Field(alias="externalId")]
    author_name: typing_extensions.Annotated[str, FieldMetadata(alias="authorName"), pydantic.Field(alias="authorName")]
    rating: int
    text: str
    reply_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="replyText"), pydantic.Field(alias="replyText")
    ] = None
    reply_status: typing_extensions.Annotated[
        ReviewReplyStatus, FieldMetadata(alias="replyStatus"), pydantic.Field(alias="replyStatus")
    ]
    platform_meta: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="platformMeta"),
        pydantic.Field(alias="platformMeta"),
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    draft_reply: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="draftReply"), pydantic.Field(alias="draftReply")
    ] = None
    draft_status: typing_extensions.Annotated[
        typing.Optional[ReviewDraftStatus], FieldMetadata(alias="draftStatus"), pydantic.Field(alias="draftStatus")
    ] = None
    draft_generated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="draftGeneratedAt"), pydantic.Field(alias="draftGeneratedAt")
    ] = None
    draft_error: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="draftError"), pydantic.Field(alias="draftError")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
