

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dependency_edge_from_type import DependencyEdgeFromType
from .dependency_edge_to_type import DependencyEdgeToType


class DependencyEdge(UniversalBaseModel):
    from_type: typing_extensions.Annotated[
        DependencyEdgeFromType, FieldMetadata(alias="fromType"), pydantic.Field(alias="fromType")
    ]
    from_id: typing_extensions.Annotated[str, FieldMetadata(alias="fromId"), pydantic.Field(alias="fromId")]
    to_type: typing_extensions.Annotated[
        DependencyEdgeToType, FieldMetadata(alias="toType"), pydantic.Field(alias="toType")
    ]
    to_id: typing_extensions.Annotated[str, FieldMetadata(alias="toId"), pydantic.Field(alias="toId")]
    relationship: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
