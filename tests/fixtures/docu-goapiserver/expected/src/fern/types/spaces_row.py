

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpacesRow(UniversalBaseModel):
    """
    A sparse row containing only the selected fields. Default fields: school_id, school_name, room_id, room_name, period, capacity, occupied_spaces, available_spaces, open_spaces, closed_spaces, unavailable_spaces, occupancy_rate.
    """

    school_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    School id.
    """

    school_name: typing.Optional[str] = None
    room_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Room id.
    """

    room_name: typing.Optional[str] = None
    period: typing.Optional[str] = None
    capacity: typing.Optional[int] = None
    occupied_spaces: typing.Optional[int] = None
    available_spaces: typing.Optional[int] = None
    open_spaces: typing.Optional[int] = None
    closed_spaces: typing.Optional[int] = None
    unavailable_spaces: typing.Optional[int] = None
    occupancy_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    Occupied spaces divided by capacity; ratio, not a percentage. Zero when capacity is zero.
    """

    is_over_enrolled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
