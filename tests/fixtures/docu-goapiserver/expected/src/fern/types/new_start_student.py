

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert import Alert


class NewStartStudent(UniversalBaseModel):
    """
    New Start Student.
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
    start_date: str
    days_to_start_date: int
    program: str
    program_tuition_weekly: float
    program_tuition_monthly: float
    pro_rate_factor_sd: float
    billing_cycle: str
    siblings: str
    service_start_end_invoice_calculated: float
    service_start_end_invoice_invoiced: float
    service_start_invoiced: str
    service_end_invoiced: str
    invoice_alert: str
    billing_plan: str
    alerts: typing.Optional[typing.List[Alert]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
