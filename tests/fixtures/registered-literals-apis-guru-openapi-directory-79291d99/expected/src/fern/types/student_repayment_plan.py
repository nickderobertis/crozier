

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .student_repayment_plan_type import StudentRepaymentPlanType


class StudentRepaymentPlan(UniversalBaseModel):
    """
    An object representing the repayment plan for the student loan
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the repayment plan as provided by the servicer.
    """

    type: typing.Optional[StudentRepaymentPlanType] = pydantic.Field(default=None)
    """
    The type of the repayment plan.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
