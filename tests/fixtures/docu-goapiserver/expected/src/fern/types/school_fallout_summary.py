

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fallout_year_summary import FalloutYearSummary


class SchoolFalloutSummary(UniversalBaseModel):
    """
    School Fallout Summary.
    """

    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    school_short_name: str
    year_summaries: typing.Optional[typing.List[FalloutYearSummary]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
