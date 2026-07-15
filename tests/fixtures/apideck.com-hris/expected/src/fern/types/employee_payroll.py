

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employee import Employee
from .payroll import Payroll


class EmployeePayroll(UniversalBaseModel):
    employee: typing.Optional[Employee] = None
    payroll: typing.Optional[Payroll] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
