

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCommentRepliesCommentsResponseCommentsItemAuthor(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier of the author
    """

    email: str = pydantic.Field()
    """
    Email of the author
    """

    name: str = pydantic.Field()
    """
    Name of the author
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
