

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .category import Category
from .contributor import Contributor
from .post import Post
from .stats import Stats
from .tag import Tag


class ListedPost(UniversalBaseModel):
    """
    Post list item with resolved categories, tags, contributors, owner, and counters.
    """

    categories: typing.List[Category] = pydantic.Field()
    """
    Resolved categories referenced by the post spec.
    """

    contributors: typing.List[Contributor] = pydantic.Field()
    """
    Users that have contributed to the post content snapshots.
    """

    owner: Contributor
    post: Post
    stats: Stats
    tags: typing.List[Tag] = pydantic.Field()
    """
    Resolved tags referenced by the post spec.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
