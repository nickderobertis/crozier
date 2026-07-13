

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .content_news_article_rss_item import ContentNewsArticleRssItem


class ContentNewsArticleRssResponse(UniversalBaseModel):
    category_filter: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="CategoryFilter")] = None
    current_pagination_token: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="CurrentPaginationToken")
    ] = None
    news_articles: typing_extensions.Annotated[
        typing.Optional[typing.List[ContentNewsArticleRssItem]], FieldMetadata(alias="NewsArticles")
    ] = None
    next_pagination_token: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="NextPaginationToken")
    ] = None
    result_count_this_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ResultCountThisPage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
