

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payroll_risk_signals_item import PayrollRiskSignalsItem
from .plaid_error import PlaidError
from .request_id import RequestId


class CreditPayrollIncomeRiskSignalsGetResponse(UniversalBaseModel):
    """
    CreditPayrollIncomeRiskSignalsGetRequest defines the response schema for `/beta/credit/payroll_income/risk_signals/get`
    """

    error: typing.Optional[PlaidError] = None
    items: typing.List[PayrollRiskSignalsItem] = pydantic.Field()
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
