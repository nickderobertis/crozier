

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lead_stage import LeadStage


class LeadStages(UniversalBaseModel):
    """
    Lead Stages.
    """

    lead_id: str = pydantic.Field()
    """
    Lead id.
    """

    stages: typing.Optional[typing.List[LeadStage]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
