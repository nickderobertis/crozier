

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_general_user import UserGeneralUser


class SocialFriendsBungieFriend(UniversalBaseModel):
    bungie_global_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bungieGlobalDisplayName"),
        pydantic.Field(alias="bungieGlobalDisplayName"),
    ] = None
    bungie_global_display_name_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bungieGlobalDisplayNameCode"),
        pydantic.Field(alias="bungieGlobalDisplayNameCode"),
    ] = None
    bungie_net_user: typing_extensions.Annotated[
        typing.Optional[UserGeneralUser], FieldMetadata(alias="bungieNetUser"), pydantic.Field(alias="bungieNetUser")
    ] = None
    last_seen_as_bungie_membership_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastSeenAsBungieMembershipType"),
        pydantic.Field(alias="lastSeenAsBungieMembershipType"),
    ] = None
    last_seen_as_membership_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastSeenAsMembershipId"),
        pydantic.Field(alias="lastSeenAsMembershipId"),
    ] = None
    online_status: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="onlineStatus"), pydantic.Field(alias="onlineStatus")
    ] = None
    online_title: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="onlineTitle"), pydantic.Field(alias="onlineTitle")
    ] = None
    relationship: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
