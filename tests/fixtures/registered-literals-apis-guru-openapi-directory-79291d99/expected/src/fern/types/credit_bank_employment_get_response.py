

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_employment_report import CreditBankEmploymentReport
from .request_id import RequestId


class CreditBankEmploymentGetResponse(UniversalBaseModel):
    """
    CreditBankEmploymentGetResponse defines the response schema for `/beta/credit/v1/bank_employment/get`.
    """

    bank_employment_reports: typing.List[CreditBankEmploymentReport] = pydantic.Field()
    """
    Bank Employment data. Each entry in the array will be a distinct bank employment report.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
