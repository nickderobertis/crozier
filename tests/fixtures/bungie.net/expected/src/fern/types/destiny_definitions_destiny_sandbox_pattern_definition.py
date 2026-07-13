

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_arrangement_region_filter_definition import (
    DestinyDefinitionsDestinyArrangementRegionFilterDefinition,
)


class DestinyDefinitionsDestinySandboxPatternDefinition(UniversalBaseModel):
    filters: typing.Optional[typing.List[DestinyDefinitionsDestinyArrangementRegionFilterDefinition]] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    pattern_global_tag_id_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="patternGlobalTagIdHash")
    ] = None
    pattern_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="patternHash")] = None
    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    weapon_content_group_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="weaponContentGroupHash")
    ] = None
    weapon_translation_group_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="weaponTranslationGroupHash")
    ] = None
    weapon_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="weaponType")] = None
    weapon_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="weaponTypeHash")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
