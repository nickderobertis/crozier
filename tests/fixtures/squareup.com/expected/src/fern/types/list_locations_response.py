

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .location import Location


class ListLocationsResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the __ListLocations__ endpoint.

    One of `errors` or `locations` is present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    The business locations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
