

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .currency import Currency
from .id import Id
from .payment_unit import PaymentUnit
from .title import Title


class EmployeeJobsItem(UniversalBaseModel):
    compensation_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The rate of pay for the employee in their current job role.
    """

    currency: typing.Optional[Currency] = None
    employee_id: typing.Optional[Id] = None
    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the employee leaves or is expected to leave their current job role.
    """

    hired_at: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the employee was hired by the organization
    """

    id: typing.Optional[Id] = None
    is_primary: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether this the employee's primary job.
    """

    location: typing.Optional[Address] = None
    payment_unit: typing.Optional[PaymentUnit] = None
    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    The position and responsibilities of the person within the organization.
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the employee starts working in their current job role.
    """

    title: typing.Optional[Title] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
