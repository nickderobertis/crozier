

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.conversation_member_input import ConversationMemberInput
from .create_team_request_channels_channels_item import CreateTeamRequestChannelsChannelsItem
from .create_team_request_channels_visibility import CreateTeamRequestChannelsVisibility


class CreateTeamRequestChannels(UniversalBaseModel):
    template_odata_bind: typing_extensions.Annotated[
        str, FieldMetadata(alias="template@odata.bind"), pydantic.Field(alias="template@odata.bind")
    ]
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    description: str
    visibility: typing.Optional[CreateTeamRequestChannelsVisibility] = None
    members: typing.Optional[typing.List[ConversationMemberInput]] = None
    channels: typing.Optional[typing.List[CreateTeamRequestChannelsChannelsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
