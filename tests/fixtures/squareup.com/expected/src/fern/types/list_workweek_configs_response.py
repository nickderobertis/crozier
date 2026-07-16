

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .workweek_config import WorkweekConfig


class ListWorkweekConfigsResponse(UniversalBaseModel):
    """
    The response to a request for a set of `WorkweekConfig` objects. The response contains
    the requested `WorkweekConfig` objects and might contain a set of `Error` objects if
    the request resulted in errors.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value supplied in the subsequent request to fetch the next page of
    `EmployeeWage` results.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    workweek_configs: typing.Optional[typing.List[WorkweekConfig]] = pydantic.Field(default=None)
    """
    A page of `EmployeeWage` results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
