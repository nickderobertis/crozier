

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SiblingDiscount(UniversalBaseModel):
    """
    Sibling Discount.
    """

    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    student_id: str = pydantic.Field()
    """
    Student id.
    """

    student_first_name: str
    student_last_name: str
    student_name: str
    family_id: str = pydantic.Field()
    """
    Family id.
    """

    status: str
    dob: str
    start_date: str
    withdrawal_date: str
    graduation_date: str
    room: str
    room_id: str = pydantic.Field()
    """
    Room id.
    """

    ems_student_status: str
    program: str
    tuition_plan: str
    billing_cycle: str
    tuition_amount: float
    net_invoice: float
    plan_status: str
    sibling_discount: str
    sibling_discount_amount: float
    sibling_discount_pct: str
    days_to_start_date: int
    parent1name: typing_extensions.Annotated[
        str, FieldMetadata(alias="parent1_name"), pydantic.Field(alias="parent1_name")
    ]
    siblings: str
    twins: str
    sibling_order: int
    sibling_twin: str
    active_siblings_in_family: int
    staff_child: str
    school_color_hex: str
    school_short_name: str
    has_birth_date_alert: bool
    has_sibling_discount_pct_alert: bool
    has_missing_sibling_discount_alert: bool
    has_unexpected_sibling_discount_alert: bool
    has_not_sibling_with_discount_alert: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
