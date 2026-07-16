

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .break_type import BreakType
from .error import Error


class ListBreakTypesResponse(UniversalBaseModel):
    """
    The response to a request for a set of `BreakType` objects. The response contains
    the requested `BreakType` objects and might contain a set of `Error` objects if
    the request resulted in errors.
    """

    break_types: typing.Optional[typing.List[BreakType]] = pydantic.Field(default=None)
    """
     A page of `BreakType` results.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value supplied in the subsequent request to fetch the next page
    of `BreakType` results.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
