

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpacesAggregate(UniversalBaseModel):
    """
    Contains the selected grouping key and requested metrics only. Grouping and metrics are flat properties on this resource.
    """

    room_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Grouping value; missing data may be represented by an empty or unknown label.
    """

    room_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Grouping value; missing data may be represented by an empty or unknown label.
    """

    school_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Grouping value; missing data may be represented by an empty or unknown label.
    """

    school_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Grouping value; missing data may be represented by an empty or unknown label.
    """

    sum_available_spaces: typing.Optional[int] = None
    sum_open_spaces: typing.Optional[int] = None
    sum_occupied_spaces: typing.Optional[int] = None
    sum_closed_spaces: typing.Optional[int] = None
    sum_unavailable_spaces: typing.Optional[int] = None
    capacity: typing.Optional[int] = None
    occupancy_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    Occupied spaces divided by capacity; ratio, not a percentage. Zero when capacity is zero.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
