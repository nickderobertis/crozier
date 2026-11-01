

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_set import NodeSet


class ListNodeSetsResponse(UniversalBaseModel):
    """
    A list of node sets.
    """

    node_sets: typing_extensions.Annotated[
        typing.List[NodeSet],
        FieldMetadata(alias="nodeSets"),
        pydantic.Field(alias="nodeSets", description="Node sets."),
    ]
    """
    Node sets.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
