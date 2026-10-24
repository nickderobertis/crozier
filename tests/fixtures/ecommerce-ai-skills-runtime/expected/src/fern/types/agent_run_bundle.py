

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_artifact import AgentArtifact
from .agent_evaluation import AgentEvaluation
from .agent_event import AgentEvent
from .agent_run import AgentRun
from .agent_task import AgentTask


class AgentRunBundle(UniversalBaseModel):
    run: AgentRun
    tasks: typing.List[AgentTask]
    artifacts: typing.List[AgentArtifact]
    events: typing.List[AgentEvent]
    evaluations: typing.List[AgentEvaluation]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
