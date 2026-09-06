

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCommentRepliesCommentsResponseCommentsItemMentionedUsersItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier of the mentioned user
    """

    email: str = pydantic.Field()
    """
    Email of the user
    """

    name: str = pydantic.Field()
    """
    Name of the  User
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
