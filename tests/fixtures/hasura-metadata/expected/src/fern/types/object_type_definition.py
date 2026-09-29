

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .object_field_definition_graph_ql_type import ObjectFieldDefinitionGraphQlType
from .type_relationship_definition import TypeRelationshipDefinition


class ObjectTypeDefinition(UniversalBaseModel):
    description: typing.Optional[str] = None
    fields: typing.List[ObjectFieldDefinitionGraphQlType]
    name: str
    relationships: typing.Optional[typing.List[TypeRelationshipDefinition]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
