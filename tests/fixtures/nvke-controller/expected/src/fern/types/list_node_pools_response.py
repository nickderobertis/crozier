

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_pool import NodePool


class ListNodePoolsResponse(UniversalBaseModel):
    """
    A list of node pools.
    """

    node_pools: typing_extensions.Annotated[
        typing.List[NodePool],
        FieldMetadata(alias="nodePools"),
        pydantic.Field(alias="nodePools", description="Node pools."),
    ]
    """
    Node pools.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
