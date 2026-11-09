

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_pay_stub_address import CreditPayStubAddress
from .pay_stub_taxpayer_id import PayStubTaxpayerId


class CreditPayStubEmployee(UniversalBaseModel):
    """
    Data about the employee.
    """

    address: CreditPayStubAddress
    marital_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Marital status of the employee - either `SINGLE` or `MARRIED`.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the employee.
    """

    taxpayer_id: PayStubTaxpayerId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
