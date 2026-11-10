

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .pslf_status import PslfStatus
from .student_loan_repayment_model import StudentLoanRepaymentModel
from .student_loan_status import StudentLoanStatus


class LiabilityOverride(UniversalBaseModel):
    """
    Used to configure Sandbox test data for the Liabilities product
    """

    balance_transfer_apr: float = pydantic.Field()
    """
    The balance transfer APR percentage value. Can only be set if `type` is `credit`.
    """

    cash_apr: float = pydantic.Field()
    """
    The cash APR percentage value. Can only be set if `type` is `credit`.
    """

    expected_payoff_date: dt.date = pydantic.Field()
    """
    Override the `expected_payoff_date` field. Can only be set if `type` is `student`.
    """

    guarantor: str = pydantic.Field()
    """
    Override the `guarantor` field. Can only be set if `type` is `student`.
    """

    interest_capitalization_grace_period_months: float = pydantic.Field()
    """
    If set, interest capitalization begins at the given number of months after loan origination. By default interest is never capitalized. Can only be set if `type` is `student`.
    """

    is_federal: bool = pydantic.Field()
    """
    Override the `is_federal` field. Can only be set if `type` is `student`.
    """

    is_overdue: bool = pydantic.Field()
    """
    Override the `is_overdue` field
    """

    last_payment_amount: float = pydantic.Field()
    """
    Override the `last_payment_amount` field. Can only be set if `type` is `credit`.
    """

    loan_name: str = pydantic.Field()
    """
    Override the `loan_name` field. Can only be set if `type` is `student`.
    """

    loan_status: StudentLoanStatus
    minimum_payment_amount: float = pydantic.Field()
    """
    Override the `minimum_payment_amount` field. Can only be set if `type` is `credit` or `student`.
    """

    nominal_apr: float = pydantic.Field()
    """
    The interest rate on the loan as a percentage. Can only be set if `type` is `student`.
    """

    origination_date: dt.date = pydantic.Field()
    """
    The date on which the loan was initially lent, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Can only be set if `type` is `student`.
    """

    payment_reference_number: str = pydantic.Field()
    """
    Override the `payment_reference_number` field. Can only be set if `type` is `student`.
    """

    principal: float = pydantic.Field()
    """
    The original loan principal. Can only be set if `type` is `student`.
    """

    pslf_status: PslfStatus
    purchase_apr: float = pydantic.Field()
    """
    The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest charges. Can only be set if `type` is `credit`.
    """

    repayment_model: StudentLoanRepaymentModel
    repayment_plan_description: str = pydantic.Field()
    """
    Override the `repayment_plan.description` field. Can only be set if `type` is `student`.
    """

    repayment_plan_type: str = pydantic.Field()
    """
    Override the `repayment_plan.type` field. Can only be set if `type` is `student`. Possible values are: `"extended graduated"`, `"extended standard"`, `"graduated"`, `"income-contingent repayment"`, `"income-based repayment"`, `"interest only"`, `"other"`, `"pay as you earn"`, `"revised pay as you earn"`, or `"standard"`.
    """

    sequence_number: str = pydantic.Field()
    """
    Override the `sequence_number` field. Can only be set if `type` is `student`.
    """

    servicer_address: Address
    special_apr: float = pydantic.Field()
    """
    The special APR percentage value. Can only be set if `type` is `credit`.
    """

    type: str = pydantic.Field()
    """
    The type of the liability object, either `credit` or `student`. Mortgages are not currently supported in the custom Sandbox.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
