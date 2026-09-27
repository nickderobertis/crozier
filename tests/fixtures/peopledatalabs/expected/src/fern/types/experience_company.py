

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .experience_company_industry import ExperienceCompanyIndustry
from .experience_company_location import ExperienceCompanyLocation
from .experience_company_size import ExperienceCompanySize


class ExperienceCompany(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Our current NOT PERSISTENT ids that tie company data to the canonical data
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name associated with the company
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website associated with the company
    """

    founded: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The year that the company was founded
    """

    size: typing.Optional[ExperienceCompanySize] = pydantic.Field(default=None)
    """
    The size range of the company
    """

    industry: typing.Optional[ExperienceCompanyIndustry] = pydantic.Field(default=None)
    """
    The industry associated with the company
    """

    linkedin_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The linkedin url associated with the company
    """

    linkedin_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The linkedin id associated with the company
    """

    facebook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The facebook url associated with the company
    """

    twitter_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The twitter associated with the company
    """

    location: typing.Optional[ExperienceCompanyLocation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
