

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PlatformIds(UniversalBaseModel):
    """
    An object containing a set of ids related to an employee
    """

    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of an employee as given by their employer
    """

    payroll_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of an employee as given by their payroll
    """

    position_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the position of the employee
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
