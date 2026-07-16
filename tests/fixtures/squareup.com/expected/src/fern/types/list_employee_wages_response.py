

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employee_wage import EmployeeWage
from .error import Error


class ListEmployeeWagesResponse(UniversalBaseModel):
    """
    The response to a request for a set of `EmployeeWage` objects. The response contains
    a set of `EmployeeWage` objects.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value supplied in the subsequent request to fetch the next page
    of `EmployeeWage` results.
    """

    employee_wages: typing.Optional[typing.List[EmployeeWage]] = pydantic.Field(default=None)
    """
    A page of `EmployeeWage` results.
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
