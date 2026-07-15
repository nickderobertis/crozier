

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .contact_gender import ContactGender
from .contact_type import ContactType
from .custom_field import CustomField
from .email import Email
from .phone_number import PhoneNumber
from .social_link import SocialLink
from .tags import Tags
from .website import Website


class Contact(UniversalBaseModel):
    active: typing.Optional[bool] = None
    addresses: typing.Optional[typing.List[Address]] = None
    birthday: typing.Optional[str] = None
    company_id: typing.Optional[str] = None
    company_name: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    current_balance: typing.Optional[float] = None
    custom_fields: typing.Optional[typing.List[CustomField]] = None
    department: typing.Optional[str] = None
    description: typing.Optional[str] = None
    email_domain: typing.Optional[str] = None
    emails: typing.Optional[typing.List[Email]] = None
    fax: typing.Optional[str] = None
    first_call_at: typing.Optional[dt.datetime] = None
    first_email_at: typing.Optional[dt.datetime] = None
    first_name: typing.Optional[str] = None
    gender: typing.Optional[ContactGender] = None
    id: typing.Optional[str] = None
    image: typing.Optional[str] = None
    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    language code according to ISO 639-1. For the United States - EN
    """

    last_activity_at: typing.Optional[dt.datetime] = None
    last_name: typing.Optional[str] = None
    lead_id: typing.Optional[str] = None
    lead_source: typing.Optional[str] = None
    middle_name: typing.Optional[str] = None
    name: str
    owner_id: typing.Optional[str] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    photo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the photo of a person.
    """

    prefix: typing.Optional[str] = None
    social_links: typing.Optional[typing.List[SocialLink]] = None
    status: typing.Optional[str] = None
    suffix: typing.Optional[str] = None
    tags: typing.Optional[Tags] = None
    title: typing.Optional[str] = None
    type: typing.Optional[ContactType] = None
    updated_at: typing.Optional[dt.datetime] = None
    websites: typing.Optional[typing.List[Website]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
