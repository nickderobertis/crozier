

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .edge_type import EdgeType


class Edge(UniversalBaseModel):
    from_: typing_extensions.Annotated[str, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    to: str
    edge_type: typing_extensions.Annotated[
        typing.Optional[EdgeType], FieldMetadata(alias="edgeType"), pydantic.Field(alias="edgeType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
