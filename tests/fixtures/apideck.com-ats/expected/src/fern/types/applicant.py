

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .anonymized import Anonymized
from .applicant_social_links_item import ApplicantSocialLinksItem
from .applicant_websites_item import ApplicantWebsitesItem
from .archived import Archived
from .created_at import CreatedAt
from .created_by import CreatedBy
from .custom_field import CustomField
from .deleted import Deleted
from .deleted_at import DeletedAt
from .deleted_by import DeletedBy
from .email import Email
from .id import Id
from .initials import Initials
from .last_interaction_at import LastInteractionAt
from .owner_id import OwnerId
from .phone_number import PhoneNumber
from .record_url import RecordUrl
from .tags import Tags
from .title import Title
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class Applicant(UniversalBaseModel):
    addresses: typing.Optional[typing.List[Address]] = None
    anonymized: typing.Optional[Anonymized] = None
    applications: typing.Optional[typing.List[str]] = None
    archived: typing.Optional[Archived] = None
    birthday: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of birth of the person.
    """

    confidential: typing.Optional[bool] = None
    coordinator_id: typing.Optional[str] = None
    cover_letter: typing.Optional[str] = None
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    custom_fields: typing.Optional[typing.List[CustomField]] = None
    cv_url: typing.Optional[str] = None
    deleted: typing.Optional[Deleted] = None
    deleted_at: typing.Optional[DeletedAt] = None
    deleted_by: typing.Optional[DeletedBy] = None
    emails: typing.Optional[typing.List[Email]] = None
    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The first name of the person.
    """

    followers: typing.Optional[typing.List[str]] = None
    headline: typing.Optional[str] = pydantic.Field(default=None)
    """
    Typically a list of previous companies where the contact has worked or schools that the contact has attended
    """

    id: typing.Optional[Id] = None
    initials: typing.Optional[Initials] = None
    job_url: typing.Optional[str] = None
    last_interaction_at: typing.Optional[LastInteractionAt] = None
    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last name of the person.
    """

    middle_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Middle name of the person.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of an applicant.
    """

    owner_id: typing.Optional[OwnerId] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    photo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the photo of a person.
    """

    position_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The PositionId the applicant applied for.
    """

    record_url: typing.Optional[RecordUrl] = None
    recruiter_id: typing.Optional[str] = None
    rejected_at: typing.Optional[dt.datetime] = None
    social_links: typing.Optional[typing.List[ApplicantSocialLinksItem]] = None
    source_id: typing.Optional[str] = None
    sourced_by: typing.Optional[str] = None
    sources: typing.Optional[typing.List[str]] = None
    stage_id: typing.Optional[str] = None
    tags: typing.Optional[Tags] = None
    title: typing.Optional[Title] = None
    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None
    websites: typing.Optional[typing.List[ApplicantWebsitesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
