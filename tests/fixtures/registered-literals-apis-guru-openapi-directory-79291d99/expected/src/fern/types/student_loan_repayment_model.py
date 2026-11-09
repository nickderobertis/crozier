

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StudentLoanRepaymentModel(UniversalBaseModel):
    """
    Student loan repayment information used to configure Sandbox test data for the Liabilities product
    """

    non_repayment_months: float = pydantic.Field()
    """
    Configures the number of months before repayment starts.
    """

    repayment_months: float = pydantic.Field()
    """
    Configures the number of months of repayments before the loan is paid off.
    """

    type: str = pydantic.Field()
    """
    The only currently supported value for this field is `standard`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
