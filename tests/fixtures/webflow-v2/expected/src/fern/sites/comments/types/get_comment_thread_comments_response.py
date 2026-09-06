

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_comment_thread_comments_response_author import GetCommentThreadCommentsResponseAuthor
from .get_comment_thread_comments_response_mentioned_users_item import (
    GetCommentThreadCommentsResponseMentionedUsersItem,
)


class GetCommentThreadCommentsResponse(UniversalBaseModel):
    """
    A comment thread represents a conversation between users on a specific page. Each comment thread has a unique identifier and can contain multiple comments. Retrieve comment replies using the replies API endpoint.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the comment thread
    """

    site_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="siteId"), pydantic.Field(alias="siteId", description="The site unique identifier")
    ]
    """
    The site unique identifier
    """

    page_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="pageId"), pydantic.Field(alias="pageId", description="The page unique identifier")
    ]
    """
    The page unique identifier
    """

    locale_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="localeId"),
        pydantic.Field(alias="localeId", description="The locale unique identifier"),
    ] = None
    """
    The locale unique identifier
    """

    item_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemId"),
        pydantic.Field(alias="itemId", description="The item unique identifier"),
    ] = None
    """
    The item unique identifier
    """

    breakpoint: str = pydantic.Field()
    """
    The breakpoint the comment was left on
    """

    url: str = pydantic.Field()
    """
    The URL of the page the comment was left on
    """

    content: str = pydantic.Field()
    """
    The content of the comment reply
    """

    is_resolved: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isResolved"),
        pydantic.Field(alias="isResolved", description="Boolean determining if the comment thread is resolved"),
    ]
    """
    Boolean determining if the comment thread is resolved
    """

    author: GetCommentThreadCommentsResponseAuthor
    mentioned_users: typing_extensions.Annotated[
        typing.List[GetCommentThreadCommentsResponseMentionedUsersItem],
        FieldMetadata(alias="mentionedUsers"),
        pydantic.Field(
            alias="mentionedUsers",
            description="List of mentioned users. This is an empty array until email notifications are sent, which can take up to 5 minutes after the comment is created.",
        ),
    ]
    """
    List of mentioned users. This is an empty array until email notifications are sent, which can take up to 5 minutes after the comment is created.
    """

    created_on: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the item was created"),
    ]
    """
    The date the item was created
    """

    last_updated: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the item was last updated"),
    ]
    """
    The date the item was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
