

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .company_info_fiscal_year_start_month import CompanyInfoFiscalYearStartMonth
from .company_info_status import CompanyInfoStatus
from .company_name import CompanyName
from .created_at import CreatedAt
from .created_by import CreatedBy
from .currency import Currency
from .email import Email
from .id import Id
from .language import Language
from .linked_tax_rate import LinkedTaxRate
from .phone_number import PhoneNumber
from .row_version import RowVersion
from .sales_tax_number import SalesTaxNumber
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class CompanyInfo(UniversalBaseModel):
    addresses: typing.Optional[typing.List[Address]] = None
    automated_sales_tax: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether sales tax is calculated automatically for the company
    """

    company_name: typing.Optional[CompanyName] = None
    company_start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date when company file was created
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    country code according to ISO 3166-1 alpha-2.
    """

    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    currency: typing.Optional[Currency] = None
    default_sales_tax: typing.Optional[LinkedTaxRate] = None
    emails: typing.Optional[typing.List[Email]] = None
    fiscal_year_start_month: typing.Optional[CompanyInfoFiscalYearStartMonth] = pydantic.Field(default=None)
    """
    The start month of fiscal year.
    """

    id: typing.Optional[Id] = None
    language: typing.Optional[Language] = None
    legal_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The legal name of the company
    """

    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    row_version: typing.Optional[RowVersion] = None
    sales_tax_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether sales tax is enabled for the company
    """

    sales_tax_number: typing.Optional[SalesTaxNumber] = None
    status: typing.Optional[CompanyInfoStatus] = pydantic.Field(default=None)
    """
    Based on the status some functionality is enabled or disabled.
    """

    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
