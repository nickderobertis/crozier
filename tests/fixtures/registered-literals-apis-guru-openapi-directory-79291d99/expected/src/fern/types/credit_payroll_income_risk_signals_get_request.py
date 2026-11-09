

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_client_id import ApiClientId
from .api_secret import ApiSecret
from .user_token import UserToken


class CreditPayrollIncomeRiskSignalsGetRequest(UniversalBaseModel):
    """
    CreditPayrollIncomeRiskSignalsGetRequest defines the request schema for `/beta/credit/payroll_income/risk_signals/get`
    """

    client_id: typing.Optional[ApiClientId] = None
    secret: typing.Optional[ApiSecret] = None
    user_token: typing.Optional[UserToken] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
