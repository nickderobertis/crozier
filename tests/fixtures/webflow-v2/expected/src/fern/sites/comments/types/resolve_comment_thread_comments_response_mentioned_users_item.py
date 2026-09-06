

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class ResolveCommentThreadCommentsResponseMentionedUsersItem(UniversalBaseModel):
    user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="The unique identifier of the mentioned user"),
    ]
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
