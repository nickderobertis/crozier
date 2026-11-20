

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .heddle_note import HeddleNote
from .shuttle_state import ShuttleState
from .warp_tension import WarpTension


class Loom(UniversalBaseModel):
    id: str
    shuttle: typing.Optional[ShuttleState] = None
    heddle: typing.Optional[HeddleNote] = None
    warp: typing.Optional[WarpTension] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
