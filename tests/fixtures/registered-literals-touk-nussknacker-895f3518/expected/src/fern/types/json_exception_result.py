

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_id import NodeId
from .result_context_json import ResultContextJson


class JsonExceptionResult(UniversalBaseModel):
    context: ResultContextJson
    node_id: typing_extensions.Annotated[
        typing.Optional[NodeId], FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId")
    ] = None
    throwable: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
