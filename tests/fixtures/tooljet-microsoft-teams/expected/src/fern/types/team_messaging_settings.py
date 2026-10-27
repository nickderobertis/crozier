

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TeamMessagingSettings(UniversalBaseModel):
    allow_user_edit_messages: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowUserEditMessages"),
        pydantic.Field(alias="allowUserEditMessages"),
    ] = None
    allow_user_delete_messages: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowUserDeleteMessages"),
        pydantic.Field(alias="allowUserDeleteMessages"),
    ] = None
    allow_owner_delete_messages: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowOwnerDeleteMessages"),
        pydantic.Field(alias="allowOwnerDeleteMessages"),
    ] = None
    allow_team_mentions: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowTeamMentions"), pydantic.Field(alias="allowTeamMentions")
    ] = None
    allow_channel_mentions: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowChannelMentions"), pydantic.Field(alias="allowChannelMentions")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
