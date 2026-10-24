

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_artifact_content import AgentArtifactContent
from .agent_artifact_kind import AgentArtifactKind


class AgentArtifact(UniversalBaseModel):
    id: str
    tenant_id: str
    run_id: str
    task_id: typing.Optional[str] = None
    kind: AgentArtifactKind
    attempt: int
    content: AgentArtifactContent
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
