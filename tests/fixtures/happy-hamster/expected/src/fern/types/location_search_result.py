

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .location import Location


class LocationSearchResult(UniversalBaseModel):
    """
    The result for a search request
    """

    coordinates: typing.Optional[typing.Any] = None
    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    List of Locations around the search query
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
