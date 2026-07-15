

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employee import Employee
from .payroll import Payroll


class EmployeePayrolls(UniversalBaseModel):
    employee: typing.Optional[Employee] = None
    payrolls: typing.Optional[typing.List[Payroll]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
