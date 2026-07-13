

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .company_vat_number import CompanyVatNumber
from .ubo import Ubo


class Company(UniversalBaseModel):
    address_main: Address = pydantic.Field()
    """
    The company's main address.
    """

    address_postal: Address = pydantic.Field()
    """
    The company's postal address.
    """

    avatar_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The public UUID of the company's avatar.
    """

    chamber_of_commerce_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's chamber of commerce number.
    """

    country: str = pydantic.Field()
    """
    The country where the company is registered.
    """

    legal_form: str = pydantic.Field()
    """
    The company's legal form.
    """

    name: str = pydantic.Field()
    """
    The company name.
    """

    signup_track_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of signup track the user is following.
    """

    subscription_type: str = pydantic.Field()
    """
    The subscription type for the company.
    """

    ubo: typing.Optional[typing.List[Ubo]] = pydantic.Field(default=None)
    """
    The names and birth dates of the company's ultimate beneficiary owners. Minimum zero, maximum four.
    """

    vat_number: typing.Optional[CompanyVatNumber] = pydantic.Field(default=None)
    """
    All the vat numbers of the company
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
