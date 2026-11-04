

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .attributes import Attributes
from .company_identifiers import CompanyIdentifiers
from .legal_type import LegalType
from .phone_number import PhoneNumber


class Company(UniversalBaseModel):
    """
    Information about the company or business. This is legal information that is used for verification.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's legal name.
    """

    merchant_category_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant category code for the account as specified by [ISO18245](https://www.iso.org/standard/33365.html). MCCs are used to classify businesses based on the goods or services they provide.
    """

    legal_type: typing.Optional[LegalType] = None
    address: typing.Optional[Address] = None
    trading_address: typing.Optional[Address] = None
    identifiers: typing.Optional[CompanyIdentifiers] = None
    phone_number: typing.Optional[PhoneNumber] = None
    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTP(S) URL of the company's website.
    """

    attributes: typing.Optional[Attributes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
