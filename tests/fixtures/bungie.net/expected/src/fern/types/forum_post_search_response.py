

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .forum_forum_recruitment_detail import ForumForumRecruitmentDetail
from .forum_poll_response import ForumPollResponse
from .forum_post_response import ForumPostResponse
from .groups_v2group_response import GroupsV2GroupResponse
from .queries_paged_query import QueriesPagedQuery
from .tags_models_contracts_tag_response import TagsModelsContractsTagResponse
from .user_general_user import UserGeneralUser


class ForumPostSearchResponse(UniversalBaseModel):
    authors: typing.Optional[typing.List[UserGeneralUser]] = None
    available_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="availablePages"), pydantic.Field(alias="availablePages")
    ] = None
    groups: typing.Optional[typing.List[GroupsV2GroupResponse]] = None
    has_more: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasMore"), pydantic.Field(alias="hasMore")
    ] = None
    polls: typing.Optional[typing.List[ForumPollResponse]] = None
    query: typing.Optional[QueriesPagedQuery] = None
    recruitment_details: typing_extensions.Annotated[
        typing.Optional[typing.List[ForumForumRecruitmentDetail]],
        FieldMetadata(alias="recruitmentDetails"),
        pydantic.Field(alias="recruitmentDetails"),
    ] = None
    related_posts: typing_extensions.Annotated[
        typing.Optional[typing.List[ForumPostResponse]],
        FieldMetadata(alias="relatedPosts"),
        pydantic.Field(alias="relatedPosts"),
    ] = None
    replacement_continuation_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="replacementContinuationToken"),
        pydantic.Field(alias="replacementContinuationToken"),
    ] = None
    results: typing.Optional[typing.List[ForumPostResponse]] = None
    searched_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[TagsModelsContractsTagResponse]],
        FieldMetadata(alias="searchedTags"),
        pydantic.Field(alias="searchedTags"),
    ] = None
    total_results: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalResults"), pydantic.Field(alias="totalResults")
    ] = None
    use_total_results: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useTotalResults"),
        pydantic.Field(
            alias="useTotalResults",
            description="If useTotalResults is true, then totalResults represents an accurate count.\r\nIf False, it does not, and may be estimated/only the size of the current page.\r\nEither way, you should probably always only trust hasMore.\r\nThis is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.",
        ),
    ] = None
    """
    If useTotalResults is true, then totalResults represents an accurate count.
    If False, it does not, and may be estimated/only the size of the current page.
    Either way, you should probably always only trust hasMore.
    This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
