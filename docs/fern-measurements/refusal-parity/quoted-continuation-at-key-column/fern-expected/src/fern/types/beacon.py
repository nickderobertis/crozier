

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lamp import Lamp


class Beacon(UniversalBaseModel):
    """
    A light on the coast that ships steer by. Each one keeps its own schedule, and its own lamp.
    """

    id: str
    lamp: Lamp
    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free text kept by the keeper
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
