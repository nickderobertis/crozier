

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SocialFriendsPlatformFriend(UniversalBaseModel):
    bungie_global_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bungieGlobalDisplayName")
    ] = None
    bungie_global_display_name_code: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bungieGlobalDisplayNameCode")
    ] = None
    bungie_net_membership_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bungieNetMembershipId")
    ] = None
    destiny_membership_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="destinyMembershipId")
    ] = None
    destiny_membership_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="destinyMembershipType")
    ] = None
    friend_platform: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="friendPlatform")] = None
    platform_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="platformDisplayName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
