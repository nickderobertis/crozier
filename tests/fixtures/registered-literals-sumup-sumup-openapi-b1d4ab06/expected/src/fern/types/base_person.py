

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .change_status import ChangeStatus
from .country_code import CountryCode
from .ownership import Ownership
from .personal_identifiers import PersonalIdentifiers
from .phone_number import PhoneNumber
from .version import Version


class BasePerson(UniversalBaseModel):
    """
    Base schema for a Person associated with a Merchant. This can be a legal representative, business owner (ultimate beneficial owner), or an officer. A legal representative is the Person who registered the Merchant with SumUp. They should always have a `user_id`.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the Person. This is a [typeid](https://github.com/sumup/typeid).
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A corresponding identity user ID for the Person, if they have a user account.
    """

    birthdate: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of birth of the individual, represented as an ISO 8601:2004 [ISO8601‑2004] YYYY-MM-DD format.
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The first name(s) of the individual.
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last name(s) of the individual.
    """

    middle_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Middle name(s) of the End-User. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.
    """

    phone_number: typing.Optional[PhoneNumber] = None
    relationships: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of roles the Person has in the Merchant or towards SumUp. A Merchant must have at least one Person with the relationship `representative`.
    """

    ownership: typing.Optional[Ownership] = None
    address: typing.Optional[Address] = None
    identifiers: typing.Optional[PersonalIdentifiers] = None
    citizenship: typing.Optional[CountryCode] = None
    nationality: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Person's nationality. May be an [ISO3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code, but legacy data may not conform to this standard.
    """

    country_of_residence: typing.Optional[str] = pydantic.Field(default=None)
    """
    An [ISO3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code representing the country where the Person resides.
    """

    version: typing.Optional[Version] = None
    change_status: typing.Optional[ChangeStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
