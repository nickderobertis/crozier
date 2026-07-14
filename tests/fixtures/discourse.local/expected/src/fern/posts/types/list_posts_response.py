

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_posts_response_latest_posts_item import ListPostsResponseLatestPostsItem


class ListPostsResponse(UniversalBaseModel):
    latest_posts: typing.Optional[typing.List[ListPostsResponseLatestPostsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
