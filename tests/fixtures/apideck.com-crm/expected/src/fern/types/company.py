

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .bank_account import BankAccount
from .company_row_type import CompanyRowType
from .currency import Currency
from .custom_field import CustomField
from .email import Email
from .first_name import FirstName
from .last_name import LastName
from .phone_number import PhoneNumber
from .social_link import SocialLink
from .tags import Tags
from .website import Website


class Company(UniversalBaseModel):
    abn_branch: typing.Optional[str] = pydantic.Field(default=None)
    """
    An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.
    """

    abn_or_tfn: typing.Optional[str] = pydantic.Field(default=None)
    """
    An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.
    """

    acn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.
    """

    addresses: typing.Optional[typing.List[Address]] = None
    annual_revenue: typing.Optional[str] = pydantic.Field(default=None)
    """
    Annual revenue
    """

    bank_accounts: typing.Optional[typing.List[BankAccount]] = None
    birthday: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of birth of the person.
    """

    created_at: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    currency: typing.Optional[Currency] = None
    custom_fields: typing.Optional[typing.List[CustomField]] = None
    deleted: typing.Optional[bool] = None
    description: typing.Optional[str] = None
    emails: typing.Optional[typing.List[Email]] = None
    fax: typing.Optional[str] = None
    first_name: typing.Optional[FirstName] = None
    id: typing.Optional[str] = None
    image: typing.Optional[str] = None
    industry: typing.Optional[str] = pydantic.Field(default=None)
    """
    Industry
    """

    interaction_count: typing.Optional[int] = None
    last_activity_at: typing.Optional[dt.datetime] = None
    last_name: typing.Optional[LastName] = None
    name: str
    number_of_employees: typing.Optional[str] = pydantic.Field(default=None)
    """
    Number of employees
    """

    owner_id: typing.Optional[str] = None
    ownership: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ownership
    """

    parent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Parent ID
    """

    payee_number: typing.Optional[str] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    read_only: typing.Optional[bool] = None
    row_type: typing.Optional[CompanyRowType] = None
    sales_tax_number: typing.Optional[str] = None
    salutation: typing.Optional[str] = pydantic.Field(default=None)
    """
    A formal salutation for the person. For example, 'Mr', 'Mrs'
    """

    social_links: typing.Optional[typing.List[SocialLink]] = None
    status: typing.Optional[str] = None
    tags: typing.Optional[Tags] = None
    updated_at: typing.Optional[dt.datetime] = None
    updated_by: typing.Optional[str] = None
    vat_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    VAT number
    """

    websites: typing.Optional[typing.List[Website]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
