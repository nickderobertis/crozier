

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .bank_account import BankAccount
from .company_name import CompanyName
from .created_at import CreatedAt
from .created_by import CreatedBy
from .currency import Currency
from .downstream_id import DownstreamId
from .email import Email
from .first_name import FirstName
from .id import Id
from .last_name import LastName
from .linked_ledger_account import LinkedLedgerAccount
from .linked_tax_rate import LinkedTaxRate
from .middle_name import MiddleName
from .phone_number import PhoneNumber
from .row_version import RowVersion
from .suffix import Suffix
from .supplier_status import SupplierStatus
from .tax_number import TaxNumber
from .title import Title
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy
from .website import Website


class Supplier(UniversalBaseModel):
    account: typing.Optional[LinkedLedgerAccount] = None
    addresses: typing.Optional[typing.List[Address]] = None
    bank_accounts: typing.Optional[typing.List[BankAccount]] = None
    company_name: typing.Optional[CompanyName] = None
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    currency: typing.Optional[Currency] = None
    display_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display ID
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name
    """

    downstream_id: typing.Optional[DownstreamId] = None
    emails: typing.Optional[typing.List[Email]] = None
    first_name: typing.Optional[FirstName] = None
    id: typing.Optional[Id] = None
    individual: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is this an individual or business supplier
    """

    last_name: typing.Optional[LastName] = None
    middle_name: typing.Optional[MiddleName] = None
    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Some notes about this supplier
    """

    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    row_version: typing.Optional[RowVersion] = None
    status: typing.Optional[SupplierStatus] = pydantic.Field(default=None)
    """
    Supplier status
    """

    suffix: typing.Optional[Suffix] = None
    tax_number: typing.Optional[TaxNumber] = None
    tax_rate: typing.Optional[LinkedTaxRate] = None
    title: typing.Optional[Title] = None
    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None
    websites: typing.Optional[typing.List[Website]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
