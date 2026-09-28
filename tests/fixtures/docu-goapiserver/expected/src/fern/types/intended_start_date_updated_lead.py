

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IntendedStartDateUpdatedLead(UniversalBaseModel):
    """
    Intended Start Date Updated Lead.
    """

    lead_id: str = pydantic.Field()
    """
    Lead id.
    """

    intended_start_date: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
