

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_income import CreditBankIncome
from .request_id import RequestId


class CreditBankIncomeGetResponse(UniversalBaseModel):
    """
    CreditBankIncomeGetResponse defines the response schema for `/credit/bank_income/get`
    """

    bank_income: typing.Optional[typing.List[CreditBankIncome]] = None
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
