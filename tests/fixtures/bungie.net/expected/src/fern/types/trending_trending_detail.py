

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .trending_trending_entry_community_creation import TrendingTrendingEntryCommunityCreation
from .trending_trending_entry_destiny_activity import TrendingTrendingEntryDestinyActivity
from .trending_trending_entry_destiny_item import TrendingTrendingEntryDestinyItem
from .trending_trending_entry_destiny_ritual import TrendingTrendingEntryDestinyRitual
from .trending_trending_entry_news import TrendingTrendingEntryNews
from .trending_trending_entry_support_article import TrendingTrendingEntrySupportArticle


class TrendingTrendingDetail(UniversalBaseModel):
    creation: typing.Optional[TrendingTrendingEntryCommunityCreation] = None
    destiny_activity: typing_extensions.Annotated[
        typing.Optional[TrendingTrendingEntryDestinyActivity],
        FieldMetadata(alias="destinyActivity"),
        pydantic.Field(alias="destinyActivity"),
    ] = None
    destiny_item: typing_extensions.Annotated[
        typing.Optional[TrendingTrendingEntryDestinyItem],
        FieldMetadata(alias="destinyItem"),
        pydantic.Field(alias="destinyItem"),
    ] = None
    destiny_ritual: typing_extensions.Annotated[
        typing.Optional[TrendingTrendingEntryDestinyRitual],
        FieldMetadata(alias="destinyRitual"),
        pydantic.Field(alias="destinyRitual"),
    ] = None
    entity_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="entityType"), pydantic.Field(alias="entityType")
    ] = None
    identifier: typing.Optional[str] = None
    news: typing.Optional[TrendingTrendingEntryNews] = None
    support: typing.Optional[TrendingTrendingEntrySupportArticle] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
