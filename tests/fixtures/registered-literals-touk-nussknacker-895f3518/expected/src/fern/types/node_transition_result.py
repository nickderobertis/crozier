

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_id import NodeId
from .result_context_json import ResultContextJson


class NodeTransitionResult(UniversalBaseModel):
    source_node_id: typing_extensions.Annotated[
        NodeId, FieldMetadata(alias="sourceNodeId"), pydantic.Field(alias="sourceNodeId")
    ]
    destination_node_id: typing_extensions.Annotated[
        typing.Optional[NodeId], FieldMetadata(alias="destinationNodeId"), pydantic.Field(alias="destinationNodeId")
    ] = None
    results: typing.Optional[typing.List[ResultContextJson]] = None
    total_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalCount"), pydantic.Field(alias="totalCount")
    ] = None
    current_throughput: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="currentThroughput"), pydantic.Field(alias="currentThroughput")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
