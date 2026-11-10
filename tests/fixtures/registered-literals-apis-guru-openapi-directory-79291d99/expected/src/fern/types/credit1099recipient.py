

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_pay_stub_address import CreditPayStubAddress


class Credit1099Recipient(UniversalBaseModel):
    """
    An object representing a recipient used in both 1099-K and 1099-MISC tax documents.
    """

    account_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account number number of recipient.
    """

    address: typing.Optional[CreditPayStubAddress] = None
    facta_filing_requirement: typing.Optional[str] = pydantic.Field(default=None)
    """
    Checked if FACTA is a filing requirement.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of recipient.
    """

    second_tin_exists: typing.Optional[str] = pydantic.Field(default=None)
    """
    Checked if 2nd TIN exists.
    """

    tin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tax identification number of recipient.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
