

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCashDrawerShiftEventsRequest(UniversalBaseModel):
    """ """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Opaque cursor for fetching the next page of results.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of resources to be returned in a page of results (200 by
    default, 1000 max).
    """

    location_id: str = pydantic.Field()
    """
    The ID of the location to list cash drawer shifts for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
