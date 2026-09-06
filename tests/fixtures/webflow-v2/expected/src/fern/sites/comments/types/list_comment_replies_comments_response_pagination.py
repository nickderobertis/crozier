

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCommentRepliesCommentsResponsePagination(UniversalBaseModel):
    limit: int = pydantic.Field()
    """
    The limit specified in the request (default 100)
    """

    offset: int = pydantic.Field()
    """
    The offset specified for pagination
    """

    total: int = pydantic.Field()
    """
    Total number of comment replies
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
