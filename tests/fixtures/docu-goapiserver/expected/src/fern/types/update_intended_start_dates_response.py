

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .intended_start_date_not_updated_lead import IntendedStartDateNotUpdatedLead
from .intended_start_date_updated_lead import IntendedStartDateUpdatedLead


class UpdateIntendedStartDatesResponse(UniversalBaseModel):
    """
    Update Intended Start Dates Response.
    """

    updated: typing.Optional[typing.List[IntendedStartDateUpdatedLead]] = None
    lead_ids_not_updated: typing.Optional[typing.List[IntendedStartDateNotUpdatedLead]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
