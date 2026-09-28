

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .company_industry import CompanyIndustry
from .company_location import CompanyLocation
from .company_size import CompanySize
from .company_type import CompanyType


class Company(UniversalBaseModel):
    affiliated_profiles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of company IDs that PDL has flagged as being affiliated and having an association to this company (either parent or child)
    """

    alternative_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of names associated with this company filtered to ensure data quality
    """

    employee_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The current integer number of employees working at the company.
    """

    facebook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary company facebook
    """

    founded: typing.Optional[int] = pydantic.Field(default=None)
    """
    The founded year of the company
    """

    headline: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's 'headline' summary
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    PDL company ID. This is currently non-persistent and generated from the company's primary linkedin username
    """

    industry: typing.Optional[CompanyIndustry] = pydantic.Field(default=None)
    """
    Self reported industry -- the enum is from linkedin's standard industries
    """

    linkedin_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary company linkedin ID
    """

    linkedin_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary company linkedin url
    """

    location: typing.Optional[CompanyLocation] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's main common name
    """

    profiles: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of all profiles associated with the company
    """

    size: typing.Optional[CompanySize] = pydantic.Field(default=None)
    """
    A range representing the number of people working at the company
    """

    summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company description
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags associated with the company
    """

    ticker: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company Ticker, (only for public companies)
    """

    twitter_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary company twitter url
    """

    type: typing.Optional[CompanyType] = pydantic.Field(default=None)
    """
    The type of the company
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary company website
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
