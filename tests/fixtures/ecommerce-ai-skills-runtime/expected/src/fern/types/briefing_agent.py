

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .briefing_agent_status import BriefingAgentStatus


class BriefingAgent(UniversalBaseModel):
    id: str
    name: str
    status: BriefingAgentStatus
    updated_at: dt.datetime
    skill_ids: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
