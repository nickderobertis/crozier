

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_result_title_status import SearchResultTitleStatus


class SearchResult(UniversalBaseModel):
    title_status: typing_extensions.Annotated[
        typing.Optional[SearchResultTitleStatus],
        FieldMetadata(alias="titleStatus"),
        pydantic.Field(
            alias="titleStatus", description="Present for title hits; manual titles must always be displayed verbatim."
        ),
    ] = None
    """
    Present for title hits; manual titles must always be displayed verbatim.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(
            alias="createdAt", description="Conversation creation time for display-time fallback localization."
        ),
    ] = None
    """
    Conversation creation time for display-time fallback localization.
    """

    conversation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="conversationId"), pydantic.Field(alias="conversationId")
    ]
    title: typing.Optional[str] = None
    project_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="projectId"), pydantic.Field(alias="projectId")
    ] = None
    snippet: typing.Optional[str] = None
    match_count: typing_extensions.Annotated[int, FieldMetadata(alias="matchCount"), pydantic.Field(alias="matchCount")]
    top_message_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="topMessageId"), pydantic.Field(alias="topMessageId")
    ] = None
    score: float
    marks: typing.Optional[typing.List[typing.List[int]]] = None
    last_message_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastMessageAt"), pydantic.Field(alias="lastMessageAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
