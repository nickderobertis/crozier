

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .search_availability_filter import SearchAvailabilityFilter


class SearchAvailabilityQuery(UniversalBaseModel):
    """
    Query conditions to search for availabilities of bookings.
    """

    filter: SearchAvailabilityFilter

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
