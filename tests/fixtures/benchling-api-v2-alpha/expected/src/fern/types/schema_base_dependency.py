

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_manifest_config import BaseManifestConfig
from .field_definitions_manifest import FieldDefinitionsManifest


class SchemaBaseDependency(BaseManifestConfig):
    field_definitions: typing_extensions.Annotated[
        typing.Optional[typing.List[FieldDefinitionsManifest]],
        FieldMetadata(alias="fieldDefinitions"),
        pydantic.Field(alias="fieldDefinitions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
