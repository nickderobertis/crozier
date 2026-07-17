

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_icon_sequence_definition import (
    DestinyDefinitionsCommonDestinyIconSequenceDefinition,
)
from .destiny_definitions_destiny_vendor_requirement_display_entry_definition import (
    DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition,
)


class DestinyDefinitionsDestinyVendorDisplayPropertiesDefinition(UniversalBaseModel):
    description: typing.Optional[str] = None
    has_icon: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasIcon"), pydantic.Field(alias="hasIcon")
    ] = None
    high_res_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="highResIcon"),
        pydantic.Field(
            alias="highResIcon",
            description="If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.",
        ),
    ] = None
    """
    If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book.
    But usually, it will be a small square image that you can use as... well, an icon.
    They are currently represented as 96px x 96px images.
    """

    icon_sequences: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsCommonDestinyIconSequenceDefinition]],
        FieldMetadata(alias="iconSequences"),
        pydantic.Field(alias="iconSequences"),
    ] = None
    large_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="largeIcon"),
        pydantic.Field(
            alias="largeIcon",
            description="I regret calling this a \"large icon\". It's more like a medium-sized image with a picture of the vendor's mug on it, trying their best to look cool. Not what one would call an icon.",
        ),
    ] = None
    """
    I regret calling this a "large icon". It's more like a medium-sized image with a picture of the vendor's mug on it, trying their best to look cool. Not what one would call an icon.
    """

    large_transparent_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="largeTransparentIcon"),
        pydantic.Field(
            alias="largeTransparentIcon",
            description='This is apparently the "Watermark". I am not certain offhand where this is actually used in the Game UI, but some people may find it useful.',
        ),
    ] = None
    """
    This is apparently the "Watermark". I am not certain offhand where this is actually used in the Game UI, but some people may find it useful.
    """

    map_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mapIcon"),
        pydantic.Field(
            alias="mapIcon",
            description="This is the icon used in the map overview, when the vendor is located on the map.",
        ),
    ] = None
    """
    This is the icon used in the map overview, when the vendor is located on the map.
    """

    name: typing.Optional[str] = None
    original_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="originalIcon"),
        pydantic.Field(
            alias="originalIcon",
            description="If we replaced the icon with something more glitzy, this is the original icon that the vendor had according to the game's content. It may be more lame and/or have less razzle-dazzle. But who am I to tell you which icon to use.",
        ),
    ] = None
    """
    If we replaced the icon with something more glitzy, this is the original icon that the vendor had according to the game's content. It may be more lame and/or have less razzle-dazzle. But who am I to tell you which icon to use.
    """

    requirements_display: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition]],
        FieldMetadata(alias="requirementsDisplay"),
        pydantic.Field(
            alias="requirementsDisplay",
            description='Vendors, in addition to expected display property data, may also show some "common requirements" as statically defined definition data. This might be when a vendor accepts a single type of currency, or when the currency is unique to the vendor and the designers wanted to show that currency when you interact with the vendor.',
        ),
    ] = None
    """
    Vendors, in addition to expected display property data, may also show some "common requirements" as statically defined definition data. This might be when a vendor accepts a single type of currency, or when the currency is unique to the vendor and the designers wanted to show that currency when you interact with the vendor.
    """

    small_transparent_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="smallTransparentIcon"),
        pydantic.Field(
            alias="smallTransparentIcon",
            description="This is the icon used in parts of the game UI such as the vendor's waypoint.",
        ),
    ] = None
    """
    This is the icon used in parts of the game UI such as the vendor's waypoint.
    """

    subtitle: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
