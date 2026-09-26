

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpaceSnapshot(UniversalBaseModel):
    """
    Space Snapshot.
    """

    capacity: int
    enrolled: int
    open_spots: int
    adjusted_open_spots: int
    closed_spots: int
    adjusted_closed_spots: int
    net_open_spots: int
    available_spots: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
