

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_document_metadata import CreditDocumentMetadata
from .credit_pay_stub_deductions import CreditPayStubDeductions
from .credit_pay_stub_earnings import CreditPayStubEarnings
from .credit_pay_stub_employee import CreditPayStubEmployee
from .credit_pay_stub_employer import CreditPayStubEmployer
from .credit_pay_stub_net_pay import CreditPayStubNetPay
from .pay_stub_pay_period_details import PayStubPayPeriodDetails


class CreditPayStub(UniversalBaseModel):
    """
    An object representing an end user's pay stub.
    """

    deductions: CreditPayStubDeductions
    document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier of the document referenced by the document metadata.
    """

    document_metadata: CreditDocumentMetadata
    earnings: CreditPayStubEarnings
    employee: CreditPayStubEmployee
    employer: CreditPayStubEmployer
    net_pay: CreditPayStubNetPay
    pay_period_details: PayStubPayPeriodDetails

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
