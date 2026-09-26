

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert import Alert


class BillingPlan(UniversalBaseModel):
    """
    Billing Plan.
    """

    id: str
    student_id: str = pydantic.Field()
    """
    Student id.
    """

    student_first_name: typing.Optional[str] = None
    student_last_name: typing.Optional[str] = None
    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    update_billing_plan_in_procare: typing.Optional[str] = None
    billing_plan_audit: typing.Optional[str] = None
    current_room_name: typing.Optional[str] = None
    current_room_id: typing.Optional[str] = None
    start_date: typing.Optional[str] = None
    transition_date: typing.Optional[str] = None
    withdrawal_date: typing.Optional[str] = None
    template_timing: str
    billing_plan_status: typing.Optional[str] = None
    current_room_program: typing.Optional[str] = None
    billing_plan: typing.Optional[str] = None
    tuition_plan_program: typing.Optional[str] = None
    transition_room_program: typing.Optional[str] = None
    billing_cycle: typing.Optional[str] = None
    invoiced_amount: typing.Optional[float] = None
    monthly_invoice_amount: typing.Optional[float] = None
    program_tuition_rate: typing.Optional[float] = None
    difference_monthly_invoice_amount: typing.Optional[float] = None
    payment_method_future: typing.Optional[str] = None
    autopay: typing.Optional[str] = None
    supply_fee_invoiced: typing.Optional[float] = None
    part_time: str
    staff_child: typing.Optional[str] = None
    siblings: str
    family_id: str = pydantic.Field()
    """
    Family id.
    """

    is_tuition_plan: bool
    color_hex: str
    short_name: str
    ems_student_status: typing.Optional[str] = None
    processing_fee_calculated: float
    processing_plan_audit: typing.Optional[str] = None
    field_labels: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    alerts: typing.Optional[typing.List[Alert]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
