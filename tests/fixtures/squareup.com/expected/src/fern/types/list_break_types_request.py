

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListBreakTypesRequest(UniversalBaseModel):
    """
    A request for a filtered set of `BreakType` objects.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pointer to the next page of `BreakType` results to fetch.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of `BreakType` results to return per page. The number can range between 1
    and 200. The default is 200.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filter the returned `BreakType` results to only those that are associated with the
    specified location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
