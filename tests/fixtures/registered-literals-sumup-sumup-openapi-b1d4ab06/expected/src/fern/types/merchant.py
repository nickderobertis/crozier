

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .business_profile import BusinessProfile
from .change_status import ChangeStatus
from .classic_merchant_identifiers import ClassicMerchantIdentifiers
from .company import Company
from .country_code import CountryCode
from .meta import Meta
from .timestamps import Timestamps
from .version import Version


class Merchant(Timestamps):
    merchant_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short unique identifier for the merchant.
    """

    organization_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the organization the merchant belongs to (if any).
    """

    business_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The business type.
    * `sole_trader`: The business is run by an self-employed individual.
    * `company`: The business is run as a company with one or more shareholders
    * `partnership`: The business is run as a company with two or more shareholders that can be also other legal entities
    * `non_profit`: The business is run as a nonprofit organization that operates for public or social benefit
    * `government_entity`: The business is state owned and operated
    """

    company: typing.Optional[Company] = None
    country: CountryCode
    business_profile: typing.Optional[BusinessProfile] = None
    avatar: typing.Optional[str] = pydantic.Field(default=None)
    """
    A user-facing small-format logo for use in dashboards and other user-facing applications. For customer-facing branding see `merchant.business_profile.branding`.
    """

    alias: typing.Optional[str] = pydantic.Field(default=None)
    """
    A user-facing name of the merchant account for use in dashboards and other user-facing applications. For customer-facing business name see `merchant.business_profile`.
    """

    default_currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217) representing the default currency for the account.
    """

    default_locale: str = pydantic.Field()
    """
    Merchant's default locale, represented as a BCP47 [RFC5646](https://datatracker.ietf.org/doc/html/rfc5646) language tag. This is typically an ISO 639-1 Alpha-2 [ISO639‑1](https://www.iso.org/iso-639-language-code) language code in lowercase and an ISO 3166-1 Alpha-2 [ISO3166‑1](https://www.iso.org/iso-3166-country-codes.html) country code in uppercase, separated by a dash. For example, en-US or fr-CA.
    In multilingual countries this is the merchant's preferred locale out of those, that are officially spoken in the country. In a countries with a single official language this will match the official language.
    """

    sandbox: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the merchant is a sandbox for testing.
    """

    meta: typing.Optional[Meta] = None
    classic: typing.Optional[ClassicMerchantIdentifiers] = None
    version: typing.Optional[Version] = None
    change_status: typing.Optional[ChangeStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
