

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .type_relationship_definition_type import TypeRelationshipDefinitionType


class TypeRelationshipDefinition(UniversalBaseModel):
    field_mapping: typing.Dict[str, str]
    name: str
    remote_table: typing.Dict[str, typing.Any]
    source: typing.Optional[str] = None
    type: TypeRelationshipDefinitionType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
