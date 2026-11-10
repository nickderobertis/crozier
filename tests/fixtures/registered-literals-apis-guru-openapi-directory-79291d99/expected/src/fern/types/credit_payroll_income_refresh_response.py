

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_payroll_income_refresh_status import CreditPayrollIncomeRefreshStatus
from .request_id import RequestId


class CreditPayrollIncomeRefreshResponse(UniversalBaseModel):
    """
    CreditPayrollIncomeRefreshResponse defines the response schema for `/credit/payroll_income/refresh`
    """

    request_id: RequestId
    verification_refresh_status: CreditPayrollIncomeRefreshStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
