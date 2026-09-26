

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .room_info_player import RoomInfoPlayer


class RoomInfoPlayers(UniversalBaseModel):
    b: typing.Optional[RoomInfoPlayer] = None
    w: typing.Optional[RoomInfoPlayer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
