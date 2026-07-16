

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyEventLocationFilter(UniversalBaseModel):
    """
    Filter events by location.
    """

    location_ids: typing.List[str] = pydantic.Field()
    """
    The [location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs for loyalty events to query.
    If multiple values are specified, the endpoint uses 
    a logical OR to combine them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
