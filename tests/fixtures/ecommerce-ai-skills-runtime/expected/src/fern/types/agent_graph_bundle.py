

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_graph import AgentGraph
from .agent_graph_version import AgentGraphVersion


class AgentGraphBundle(UniversalBaseModel):
    graph: AgentGraph
    versions: typing.List[AgentGraphVersion]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
