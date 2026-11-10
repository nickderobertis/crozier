

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_pay_stub_address import CreditPayStubAddress


class CreditPayStubEmployer(UniversalBaseModel):
    """
    Information about the employer on the pay stub.
    """

    address: CreditPayStubAddress
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the employer on the pay stub.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
