

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_definition_read import SourceDefinitionRead


class SourceDefinitionReadList(UniversalBaseModel):
    source_definitions: typing_extensions.Annotated[
        typing.List[SourceDefinitionRead],
        FieldMetadata(alias="sourceDefinitions"),
        pydantic.Field(alias="sourceDefinitions"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
