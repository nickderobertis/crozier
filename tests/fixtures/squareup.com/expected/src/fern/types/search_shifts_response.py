

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .shift import Shift


class SearchShiftsResponse(UniversalBaseModel):
    """
    The response to a request for `Shift` objects. The response contains
    the requested `Shift` objects and might contain a set of `Error` objects if
    the request resulted in errors.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    An opaque cursor for fetching the next page.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    shifts: typing.Optional[typing.List[Shift]] = pydantic.Field(default=None)
    """
    Shifts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
