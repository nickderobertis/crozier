

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_general_user import UserGeneralUser


class ForumForumRecruitmentDetail(UniversalBaseModel):
    fireteam: typing_extensions.Annotated[
        typing.Optional[typing.List[UserGeneralUser]], FieldMetadata(alias="Fireteam")
    ] = None
    approved: typing.Optional[bool] = None
    conversation_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="conversationId")] = None
    intensity: typing.Optional[int] = None
    kicked_player_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="kickedPlayerIds")
    ] = None
    microphone_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="microphoneRequired")
    ] = None
    player_slots_remaining: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="playerSlotsRemaining")
    ] = None
    player_slots_total: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="playerSlotsTotal")] = (
        None
    )
    tone: typing.Optional[int] = None
    topic_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="topicId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
