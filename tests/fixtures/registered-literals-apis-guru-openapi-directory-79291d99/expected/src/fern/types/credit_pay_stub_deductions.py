

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pay_stub_deductions_breakdown import PayStubDeductionsBreakdown
from .pay_stub_deductions_total import PayStubDeductionsTotal


class CreditPayStubDeductions(UniversalBaseModel):
    """
    An object with the deduction information found on a pay stub.
    """

    breakdown: typing.List[PayStubDeductionsBreakdown]
    total: PayStubDeductionsTotal

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
