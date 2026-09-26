

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .game_record_participant import GameRecordParticipant
from .game_record_source import GameRecordSource
from .game_record_status import GameRecordStatus
from .game_record_visibility import GameRecordVisibility
from .game_result_payload import GameResultPayload


class GameRecordSummary(UniversalBaseModel):
    id: str
    room_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="roomId"), pydantic.Field(alias="roomId")
    ] = None
    source: GameRecordSource
    visibility: GameRecordVisibility
    public_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publicId"), pydantic.Field(alias="publicId")
    ] = None
    status: GameRecordStatus
    result: typing.Optional[GameResultPayload] = None
    participants: typing.List[GameRecordParticipant]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    finished_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="finishedAt"), pydantic.Field(alias="finishedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
