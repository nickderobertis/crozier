

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyRaceDefinition(UniversalBaseModel):
    """
    In Destiny, "Races" are really more like "Species". Sort of. I mean, are the Awoken a separate species from humans? I'm not sure. But either way, they're defined here. You'll see Exo, Awoken, and Human as examples of these Species. Players will choose one for their character.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    gendered_race_names: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="genderedRaceNames"),
        pydantic.Field(
            alias="genderedRaceNames",
            description="A localized string referring to the singular form of the Race's name when referred to in gendered form. Keyed by the DestinyGender.",
        ),
    ] = None
    """
    A localized string referring to the singular form of the Race's name when referred to in gendered form. Keyed by the DestinyGender.
    """

    gendered_race_names_by_gender_hash: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="genderedRaceNamesByGenderHash"),
        pydantic.Field(alias="genderedRaceNamesByGenderHash"),
    ] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    race_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="raceType"),
        pydantic.Field(
            alias="raceType",
            description="An enumeration defining the existing, known Races/Species for player characters. This value will be the enum value matching this definition.",
        ),
    ] = None
    """
    An enumeration defining the existing, known Races/Species for player characters. This value will be the enum value matching this definition.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
