

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EmployeeTimeOff(UniversalBaseModel):
    """
    Employee Time Off.
    """

    balance: int
    balance_change: int
    effective_time: str
    employee_id: str = pydantic.Field()
    """
    Employee id.
    """

    event_description: str
    event_type: str
    policy_name: str
    time_off_type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
