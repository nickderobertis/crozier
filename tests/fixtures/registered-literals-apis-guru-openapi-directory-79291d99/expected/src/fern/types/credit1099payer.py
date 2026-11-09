

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_pay_stub_address import CreditPayStubAddress


class Credit1099Payer(UniversalBaseModel):
    """
    An object representing a payer used by 1099-MISC tax documents.
    """

    address: typing.Optional[CreditPayStubAddress] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of payer.
    """

    telephone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Telephone number of payer.
    """

    tin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tax identification number of payer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
