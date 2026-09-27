

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .school_location import SchoolLocation
from .school_type import SchoolType


class School(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Our current NOT PERSISTENT ids that tie company data to the canonical data
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name associated with the school
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website associated with the school, could include subdomains
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website associated with the school
    """

    type: typing.Optional[SchoolType] = pydantic.Field(default=None)
    """
    The type of school
    """

    linkedin_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The linkedin url associated with the school
    """

    linkedin_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The linkedin ID associated with the school
    """

    facebook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The facebook url associated with the school
    """

    twitter_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The twitter url associated with the school
    """

    location: typing.Optional[SchoolLocation] = pydantic.Field(default=None)
    """
    The location associated with the school
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
