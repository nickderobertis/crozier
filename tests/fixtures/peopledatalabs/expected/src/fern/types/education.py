

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .school import School


class Education(UniversalBaseModel):
    degrees: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of canonical degrees associated with this education object
    """

    majors: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of majors associated with this education object
    """

    minors: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of minors associated with this education object
    """

    school: typing.Optional[School] = pydantic.Field(default=None)
    """
    A dictionary of information for the associated school
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Indicates the start period of the object
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Indicates the end period of the object
    """

    gpa: typing.Optional[float] = pydantic.Field(default=None)
    """
    The gpa associated with the given degree
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
