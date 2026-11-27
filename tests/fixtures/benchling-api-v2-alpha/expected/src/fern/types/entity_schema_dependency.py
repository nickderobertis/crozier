

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .entity_schema_dependency_type import EntitySchemaDependencyType
from .schema_base_dependency import SchemaBaseDependency
from .schema_dependency_subtypes import SchemaDependencySubtypes


class EntitySchemaDependency(SchemaBaseDependency):
    subtype: typing.Optional[SchemaDependencySubtypes] = None
    type: typing.Optional[EntitySchemaDependencyType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
