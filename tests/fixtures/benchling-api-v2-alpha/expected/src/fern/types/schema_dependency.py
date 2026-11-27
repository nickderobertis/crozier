

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .schema_base_dependency import SchemaBaseDependency
from .schema_dependency_types import SchemaDependencyTypes


class SchemaDependency(SchemaBaseDependency):
    type: typing.Optional[SchemaDependencyTypes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
