

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employee_employment_role_sub_type import EmployeeEmploymentRoleSubType
from .employee_employment_role_type import EmployeeEmploymentRoleType


class EmployeeEmploymentRole(UniversalBaseModel):
    sub_type: typing.Optional[EmployeeEmploymentRoleSubType] = pydantic.Field(default=None)
    """
    The work schedule of the employee.
    """

    type: typing.Optional[EmployeeEmploymentRoleType] = pydantic.Field(default=None)
    """
    The type of employment relationship the employee has with the organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
