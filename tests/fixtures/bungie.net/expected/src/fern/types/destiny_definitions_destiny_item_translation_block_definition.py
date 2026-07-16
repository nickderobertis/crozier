

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_gear_art_arrangement_reference import (
    DestinyDefinitionsDestinyGearArtArrangementReference,
)
from .destiny_dye_reference import DestinyDyeReference


class DestinyDefinitionsDestinyItemTranslationBlockDefinition(UniversalBaseModel):
    """
    This Block defines the rendering data associated with the item, if any.
    """

    arrangements: typing.Optional[typing.List[DestinyDefinitionsDestinyGearArtArrangementReference]] = None
    custom_dyes: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDyeReference]],
        FieldMetadata(alias="customDyes"),
        pydantic.Field(alias="customDyes"),
    ] = None
    default_dyes: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDyeReference]],
        FieldMetadata(alias="defaultDyes"),
        pydantic.Field(alias="defaultDyes"),
    ] = None
    has_geometry: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasGeometry"), pydantic.Field(alias="hasGeometry")
    ] = None
    locked_dyes: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDyeReference]],
        FieldMetadata(alias="lockedDyes"),
        pydantic.Field(alias="lockedDyes"),
    ] = None
    weapon_pattern_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="weaponPatternHash"), pydantic.Field(alias="weaponPatternHash")
    ] = None
    weapon_pattern_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="weaponPatternIdentifier"),
        pydantic.Field(alias="weaponPatternIdentifier"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
