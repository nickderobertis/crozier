

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payroll_item import PayrollItem
from .plaid_error import PlaidError
from .request_id import RequestId


class CreditPayrollIncomeGetResponse(UniversalBaseModel):
    """
    Defines the response body for `/credit/payroll_income/get`.
    """

    error: typing.Optional[PlaidError] = None
    items: typing.List[PayrollItem] = pydantic.Field()
    """
    Array of payroll items.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
