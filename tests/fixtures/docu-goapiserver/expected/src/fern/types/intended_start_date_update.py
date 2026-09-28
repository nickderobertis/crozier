

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .intended_start_date_update_intended_start_date import IntendedStartDateUpdateIntendedStartDate


class IntendedStartDateUpdate(UniversalBaseModel):
    """
    Intended Start Date Update.
    """

    lead_ids: typing.List[str]
    intended_start_date: IntendedStartDateUpdateIntendedStartDate = pydantic.Field()
    """
    TBD or a strictly future calendar date in YYYY-MM-DD; surrounding whitespace is trimmed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
