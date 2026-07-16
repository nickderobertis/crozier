

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TrendingTrendingEntryCommunityCreation(UniversalBaseModel):
    author: typing.Optional[str] = None
    author_membership_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="authorMembershipId"), pydantic.Field(alias="authorMembershipId")
    ] = None
    body: typing.Optional[str] = None
    media: typing.Optional[str] = None
    post_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="postId"), pydantic.Field(alias="postId")
    ] = None
    title: typing.Optional[str] = None
    upvotes: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
