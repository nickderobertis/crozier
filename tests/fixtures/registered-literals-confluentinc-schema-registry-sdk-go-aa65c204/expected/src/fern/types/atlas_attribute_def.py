

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .atlas_attribute_def_cardinality import AtlasAttributeDefCardinality
from .atlas_attribute_def_index_type import AtlasAttributeDefIndexType
from .atlas_constraint_def import AtlasConstraintDef


class AtlasAttributeDef(UniversalBaseModel):
    name: typing.Optional[str] = None
    type_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeName"), pydantic.Field(alias="typeName")
    ] = None
    is_optional: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isOptional"), pydantic.Field(alias="isOptional")
    ] = None
    cardinality: typing.Optional[AtlasAttributeDefCardinality] = None
    values_min_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="valuesMinCount"), pydantic.Field(alias="valuesMinCount")
    ] = None
    values_max_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="valuesMaxCount"), pydantic.Field(alias="valuesMaxCount")
    ] = None
    is_unique: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isUnique"), pydantic.Field(alias="isUnique")
    ] = None
    is_indexable: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isIndexable"), pydantic.Field(alias="isIndexable")
    ] = None
    include_in_notification: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="includeInNotification"),
        pydantic.Field(alias="includeInNotification"),
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="defaultValue"), pydantic.Field(alias="defaultValue")
    ] = None
    description: typing.Optional[str] = None
    search_weight: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="searchWeight"), pydantic.Field(alias="searchWeight")
    ] = None
    index_type: typing_extensions.Annotated[
        typing.Optional[AtlasAttributeDefIndexType], FieldMetadata(alias="indexType"), pydantic.Field(alias="indexType")
    ] = None
    constraints: typing.Optional[typing.List[AtlasConstraintDef]] = None
    options: typing.Optional[typing.Dict[str, str]] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
