

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert import Alert


class WithdrawalStudent(UniversalBaseModel):
    """
    Withdrawal Student.
    """

    student_id: str = pydantic.Field()
    """
    Student id.
    """

    student_name: str
    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    procare_student_status: str
    ems_student_status: str
    room_id: str = pydantic.Field()
    """
    Room id.
    """

    room_name: str
    billing_plan: str
    billing_cycle: str
    pro_rate_factor_wd: float
    withdrawal_date: str
    days_to_withdrawal_date: int
    plan_status: str
    service_start_end_invoice_calculated: float
    service_start_end_invoice_invoiced: float
    service_end_invoiced: str
    invoice_alert: str
    deposit_applied: float
    deposit_collected: float
    start_date: str
    alerts: typing.Optional[typing.List[Alert]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
