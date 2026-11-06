

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .coordinates import Coordinates
from .location_details import LocationDetails
from .location_id import LocationId
from .occupancy import Occupancy


class Location(UniversalBaseModel):
    """
    A physical location which represents a supermarket or similar
    """

    id: LocationId
    name: str
    favorite: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this Location is a favorite of the currently logged in user.
    (Will be null if the user is not logged in.)
    """

    details: typing.Optional[LocationDetails] = None
    coordinates: Coordinates
    occupancy: Occupancy
    address: Address

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
