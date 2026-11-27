

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .constraint_create import ConstraintCreate
from .entity_schema_base_auth_parent_option import EntitySchemaBaseAuthParentOption
from .entity_schema_base_containable_type import EntitySchemaBaseContainableType
from .entity_schema_base_type import EntitySchemaBaseType
from .field_create import FieldCreate
from .naming_strategy import NamingStrategy


class EntitySchemaBase(UniversalBaseModel):
    auth_parent_option: typing_extensions.Annotated[
        typing.Optional[EntitySchemaBaseAuthParentOption],
        FieldMetadata(alias="authParentOption"),
        pydantic.Field(alias="authParentOption"),
    ] = None
    constraint: typing.Optional[ConstraintCreate] = None
    containable_type: typing_extensions.Annotated[
        typing.Optional[EntitySchemaBaseContainableType],
        FieldMetadata(alias="containableType"),
        pydantic.Field(alias="containableType"),
    ] = None
    fields: typing.Optional[typing.List[FieldCreate]] = None
    include_registry_id_in_chips: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="includeRegistryIdInChips"),
        pydantic.Field(alias="includeRegistryIdInChips"),
    ] = None
    is_containable: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isContainable"), pydantic.Field(alias="isContainable")
    ] = None
    labeling_strategies: typing_extensions.Annotated[
        typing.Optional[typing.List[NamingStrategy]],
        FieldMetadata(alias="labelingStrategies"),
        pydantic.Field(alias="labelingStrategies"),
    ] = None
    mixture_schema_config: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="mixtureSchemaConfig"),
        pydantic.Field(alias="mixtureSchemaConfig"),
    ] = None
    name: typing.Optional[str] = None
    prefix: typing.Optional[str] = None
    registry_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="registryId"), pydantic.Field(alias="registryId")
    ] = None
    result_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resultSchemaId"), pydantic.Field(alias="resultSchemaId")
    ] = None
    sequence_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sequenceType"), pydantic.Field(alias="sequenceType")
    ] = None
    should_create_as_oligo: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="shouldCreateAsOligo"), pydantic.Field(alias="shouldCreateAsOligo")
    ] = None
    should_order_name_parts_by_sequence: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="shouldOrderNamePartsBySequence"),
        pydantic.Field(alias="shouldOrderNamePartsBySequence"),
    ] = None
    show_residues: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showResidues"), pydantic.Field(alias="showResidues")
    ] = None
    type: typing.Optional[EntitySchemaBaseType] = None
    use_organization_collection_alias_for_display_label: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useOrganizationCollectionAliasForDisplayLabel"),
        pydantic.Field(alias="useOrganizationCollectionAliasForDisplayLabel"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
