

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency import Currency
from .employee_compensations_item_flsa_status import EmployeeCompensationsItemFlsaStatus
from .id import Id
from .payment_unit import PaymentUnit


class EmployeeCompensationsItem(UniversalBaseModel):
    currency: typing.Optional[Currency] = None
    effective_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date on which a change to an employee's compensation takes effect.
    """

    flsa_status: typing.Optional[EmployeeCompensationsItemFlsaStatus] = pydantic.Field(default=None)
    """
    The FLSA status for this compensation.
    """

    id: typing.Optional[Id] = None
    job_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the job to which the compensation belongs.
    """

    payment_unit: typing.Optional[PaymentUnit] = None
    rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount paid per payment unit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
