

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .game_record_seat import GameRecordSeat


class GameRecordParticipant(UniversalBaseModel):
    seat: typing.Optional[GameRecordSeat] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    display_name_snapshot: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayNameSnapshot"), pydantic.Field(alias="displayNameSnapshot")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
