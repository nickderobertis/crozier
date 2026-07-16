

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchResponseGroupedSearchResult(UniversalBaseModel):
    can_create_topic: bool
    category_ids: typing.List[typing.Any]
    error: typing.Optional[str] = None
    group_ids: typing.List[typing.Any]
    more_categories: typing.Optional[str] = None
    more_full_page_results: typing.Optional[str] = None
    more_posts: typing.Optional[str] = None
    more_users: typing.Optional[str] = None
    post_ids: typing.List[typing.Any]
    search_log_id: int
    tag_ids: typing.List[typing.Any]
    term: str
    user_ids: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
