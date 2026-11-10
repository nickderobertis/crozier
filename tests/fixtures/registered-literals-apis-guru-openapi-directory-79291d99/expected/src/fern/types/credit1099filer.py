

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_pay_stub_address import CreditPayStubAddress


class Credit1099Filer(UniversalBaseModel):
    """
    An object representing a filer used by 1099-K tax documents.
    """

    address: typing.Optional[CreditPayStubAddress] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of filer.
    """

    tin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tax identification number of filer.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    One of the following values will be provided: Payment Settlement Entity (PSE), Electronic Payment Facilitator (EPF), Other Third Party
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
