

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action import Action
from .agent_run import AgentRun
from .briefing_agent import BriefingAgent
from .briefing_metric import BriefingMetric
from .operating_briefing_evidence import OperatingBriefingEvidence
from .operating_briefing_platform import OperatingBriefingPlatform


class OperatingBriefing(UniversalBaseModel):
    platform: OperatingBriefingPlatform
    evidence: OperatingBriefingEvidence
    metrics: typing.List[BriefingMetric]
    latest_run: typing.Optional[AgentRun] = None
    brief_run_id: typing.Optional[str] = None
    executive_summary: typing.Optional[str] = None
    priorities: typing.List[typing.Dict[str, typing.Any]]
    risks: typing.List[typing.Dict[str, typing.Any]]
    limitations: typing.List[str]
    agents: typing.List[BriefingAgent]
    approvals: typing.List[Action]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
