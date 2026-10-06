

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_dto import PostDto
from .posts_response_limit import PostsResponseLimit
from .posts_response_offset import PostsResponseOffset


class PostsResponse(UniversalBaseModel):
    """
    Модель ответа для получения постов
    """

    posts: typing.Optional[typing.List[PostDto]] = None
    offset: typing.Optional[PostsResponseOffset] = None
    limit: typing.Optional[PostsResponseLimit] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
