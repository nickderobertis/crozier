

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .experience_company import ExperienceCompany
from .title import Title


class Experience(UniversalBaseModel):
    title: typing.Optional[Title] = pydantic.Field(default=None)
    """
    A dictionary object that provides a raw title, canonized title, and level
    """

    company: typing.Optional[ExperienceCompany] = pydantic.Field(default=None)
    """
    A dictionary of information for the associated company
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Indicates the start period of the object. Can be accurate to the day (YYYY-MM-DD), month (YYYY-MM) or year (YYYY)
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Indicates the end period of the object
    """

    location_names: typing.Optional[str] = pydantic.Field(default=None)
    """
    Canonical locations associated with this particular job/experience object (where the person is working, which may or may not be where the company is headquartered.)
    """

    is_primary: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the experience is the primary experience object in our dataset. This experience object will exist in the job_XXX fields
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
