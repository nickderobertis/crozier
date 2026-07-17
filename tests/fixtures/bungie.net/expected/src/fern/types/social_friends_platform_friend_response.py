

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .social_friends_platform_friend import SocialFriendsPlatformFriend


class SocialFriendsPlatformFriendResponse(UniversalBaseModel):
    current_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentPage"), pydantic.Field(alias="currentPage")
    ] = None
    has_more: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasMore"), pydantic.Field(alias="hasMore")
    ] = None
    items_per_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="itemsPerPage"), pydantic.Field(alias="itemsPerPage")
    ] = None
    platform_friends: typing_extensions.Annotated[
        typing.Optional[typing.List[SocialFriendsPlatformFriend]],
        FieldMetadata(alias="platformFriends"),
        pydantic.Field(alias="platformFriends"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
