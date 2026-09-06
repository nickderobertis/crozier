

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_member_response import GuildMemberResponse


class InviteStageInstanceResponse(UniversalBaseModel):
    topic: str
    participant_count: typing.Optional[int] = None
    speaker_count: typing.Optional[int] = None
    members: typing.Optional[typing.List[GuildMemberResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
