

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node import Node
from .rel_type import RelType


class Relation(UniversalBaseModel):
    source: typing.Optional[Node] = None
    target: typing.Optional[Node] = None
    rel_type: typing_extensions.Annotated[
        typing.Optional[RelType], FieldMetadata(alias="relType"), pydantic.Field(alias="relType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
