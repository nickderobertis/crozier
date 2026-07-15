

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employees_filter_employment_status import EmployeesFilterEmploymentStatus


class EmployeesFilter(UniversalBaseModel):
    company_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company ID to filter on
    """

    department_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the department to filter on
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email to filter on
    """

    employee_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Employee number to filter on
    """

    employment_status: typing.Optional[EmployeesFilterEmploymentStatus] = pydantic.Field(default=None)
    """
    Employment status to filter on
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    First Name to filter on
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last Name to filter on
    """

    manager_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Manager id to filter on
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Job title to filter on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
