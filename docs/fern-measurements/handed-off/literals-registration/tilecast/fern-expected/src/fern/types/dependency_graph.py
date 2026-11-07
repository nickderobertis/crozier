

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dependency_edge import DependencyEdge
from .dependency_node import DependencyNode


class DependencyGraph(UniversalBaseModel):
    nodes: typing.List[DependencyNode]
    edges: typing.List[DependencyEdge]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
