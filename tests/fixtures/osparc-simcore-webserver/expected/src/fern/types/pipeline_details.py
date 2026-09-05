

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .node_state import NodeState


class PipelineDetails(UniversalBaseModel):
    adjacency_list: typing.Dict[str, typing.List[str]] = pydantic.Field()
    """
    The adjacency list of the current pipeline in terms of {NodeID: [successor NodeID]}
    """

    progress: typing.Optional[float] = pydantic.Field(default=None)
    """
    the progress of the pipeline (None if there are no computational tasks)
    """

    node_states: typing.Dict[str, NodeState] = pydantic.Field()
    """
    The states of each of the computational nodes in the pipeline
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
