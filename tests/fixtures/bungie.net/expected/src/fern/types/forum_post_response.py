

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ignores_ignore_response import IgnoresIgnoreResponse


class ForumPostResponse(UniversalBaseModel):
    is_pinned: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="IsPinned")] = None
    ignore_status: typing_extensions.Annotated[
        typing.Optional[IgnoresIgnoreResponse], FieldMetadata(alias="ignoreStatus")
    ] = None
    is_active: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isActive")] = None
    is_announcement: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isAnnouncement")] = None
    last_reply_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastReplyTimestamp")
    ] = None
    latest_reply_author_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="latestReplyAuthorId")
    ] = None
    latest_reply_post_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="latestReplyPostId")
    ] = None
    locale: typing.Optional[str] = None
    popularity: typing.Optional[int] = None
    thumbnail: typing.Optional[str] = None
    url_media_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="urlMediaType")] = None
    user_has_muted_post: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="userHasMutedPost")] = (
        None
    )
    user_has_rated: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="userHasRated")] = None
    user_rating: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="userRating")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
