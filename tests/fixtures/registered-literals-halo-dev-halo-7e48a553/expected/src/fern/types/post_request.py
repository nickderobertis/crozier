

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_update_param import ContentUpdateParam
from .post import Post


class PostRequest(UniversalBaseModel):
    """
    Post editor payload containing the post extension and its editable content.
    """

    content: ContentUpdateParam
    post: Post

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
