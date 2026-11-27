

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .entity_schema_base import EntitySchemaBase
from .entity_schema_summary import EntitySchemaSummary


class EntitySchema(EntitySchemaBase, EntitySchemaSummary):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
