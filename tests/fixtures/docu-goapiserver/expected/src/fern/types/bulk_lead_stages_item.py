

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_lead_stages_request import UpdateLeadStagesRequest


class BulkLeadStagesItem(UniversalBaseModel):
    """
    Bulk Lead Stages Item.
    """

    lead_id: str = pydantic.Field()
    """
    Lead id.
    """

    stages: UpdateLeadStagesRequest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
