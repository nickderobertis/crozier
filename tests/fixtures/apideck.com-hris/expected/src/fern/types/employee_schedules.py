

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employee import Employee
from .schedule import Schedule


class EmployeeSchedules(UniversalBaseModel):
    employee: typing.Optional[Employee] = None
    schedules: typing.Optional[typing.List[Schedule]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
