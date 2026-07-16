

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class EmployeeWage(UniversalBaseModel):
    """
    The hourly wage rate that an employee earns on a `Shift` for doing the job
    specified by the `title` property of this object. Deprecated at version 2020-08-26. Use `TeamMemberWage` instead.
    """

    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `Employee` that this wage is assigned to.
    """

    hourly_rate: typing.Optional[Money] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID for this object.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job title that this wage relates to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
