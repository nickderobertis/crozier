

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .school_fallout_summary import SchoolFalloutSummary


class PreRegistrationFalloutReport(UniversalBaseModel):
    """
    Pre Registration Fallout Report.
    """

    years: typing.Optional[typing.List[int]] = None
    school_summaries: typing.Optional[typing.List[SchoolFalloutSummary]] = None
    total_summary: SchoolFalloutSummary

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
