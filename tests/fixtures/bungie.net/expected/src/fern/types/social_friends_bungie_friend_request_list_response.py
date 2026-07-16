

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .social_friends_bungie_friend import SocialFriendsBungieFriend


class SocialFriendsBungieFriendRequestListResponse(UniversalBaseModel):
    incoming_requests: typing_extensions.Annotated[
        typing.Optional[typing.List[SocialFriendsBungieFriend]],
        FieldMetadata(alias="incomingRequests"),
        pydantic.Field(alias="incomingRequests"),
    ] = None
    outgoing_requests: typing_extensions.Annotated[
        typing.Optional[typing.List[SocialFriendsBungieFriend]],
        FieldMetadata(alias="outgoingRequests"),
        pydantic.Field(alias="outgoingRequests"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
