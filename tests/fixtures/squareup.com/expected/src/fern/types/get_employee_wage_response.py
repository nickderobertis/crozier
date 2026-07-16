

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employee_wage import EmployeeWage
from .error import Error


class GetEmployeeWageResponse(UniversalBaseModel):
    """
    A response to a request to get an `EmployeeWage`. The response contains
    the requested `EmployeeWage` objects and might contain a set of `Error` objects if
    the request resulted in errors.
    """

    employee_wage: typing.Optional[EmployeeWage] = None
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
