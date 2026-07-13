

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .currency import Currency
from .custom_field import CustomField
from .email import Email
from .phone_number import PhoneNumber
from .social_link import SocialLink
from .tags import Tags
from .website import Website


class Lead(UniversalBaseModel):
    addresses: typing.Optional[typing.List[Address]] = None
    company_id: typing.Optional[str] = None
    company_name: typing.Optional[str] = None
    contact_id: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    currency: typing.Optional[Currency] = None
    custom_fields: typing.Optional[typing.List[CustomField]] = None
    description: typing.Optional[str] = None
    emails: typing.Optional[typing.List[Email]] = None
    fax: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    id: typing.Optional[str] = None
    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    language code according to ISO 639-1. For the United States - EN
    """

    last_name: typing.Optional[str] = None
    lead_source: typing.Optional[str] = None
    monetary_amount: typing.Optional[float] = None
    name: str
    owner_id: typing.Optional[str] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    prefix: typing.Optional[str] = None
    social_links: typing.Optional[typing.List[SocialLink]] = None
    status: typing.Optional[str] = None
    tags: typing.Optional[Tags] = None
    title: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None
    websites: typing.Optional[typing.List[Website]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
