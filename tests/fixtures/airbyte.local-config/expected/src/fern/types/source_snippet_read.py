

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_definition_id import SourceDefinitionId
from .source_id import SourceId


class SourceSnippetRead(UniversalBaseModel):
    icon: typing.Optional[str] = None
    name: str
    source_definition_id: typing_extensions.Annotated[
        SourceDefinitionId, FieldMetadata(alias="sourceDefinitionId"), pydantic.Field(alias="sourceDefinitionId")
    ]
    source_id: typing_extensions.Annotated[SourceId, FieldMetadata(alias="sourceId"), pydantic.Field(alias="sourceId")]
    source_name: typing_extensions.Annotated[str, FieldMetadata(alias="sourceName"), pydantic.Field(alias="sourceName")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
