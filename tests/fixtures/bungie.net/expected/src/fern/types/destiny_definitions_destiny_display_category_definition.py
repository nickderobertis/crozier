

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyDisplayCategoryDefinition(UniversalBaseModel):
    """
    Display Categories are different from "categories" in that these are specifically for visual grouping and display of categories in Vendor UI. The "categories" structure is for validation of the contained items, and can be categorized entirely separately from "Display Categories", there need be and often will be no meaningful relationship between the two.
    """

    display_category_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="displayCategoryHash")
    ] = None
    display_in_banner: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="displayInBanner")] = (
        pydantic.Field(default=None)
    )
    """
    If true, this category should be displayed in the "Banner" section of the vendor's UI.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = None
    display_style_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="displayStyleHash")] = (
        pydantic.Field(default=None)
    )
    """
    An indicator of how the category will be displayed in the UI. It's up to you to do something cool or interesting in response to this, or just to treat it as a normal category.
    """

    display_style_identifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayStyleIdentifier")
    ] = pydantic.Field(default=None)
    """
    An indicator of how the category will be displayed in the UI. It's up to you to do something cool or interesting in response to this, or just to treat it as a normal category.
    """

    identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string identifier for the display category.
    """

    index: typing.Optional[int] = None
    progression_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="progressionHash")] = (
        pydantic.Field(default=None)
    )
    """
    If it exists, this is the hash identifier of a DestinyProgressionDefinition that represents the progression to show on this display category.
    Specific categories can now have thier own distinct progression, apparently. So that's cool.
    """

    sort_order: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="sortOrder")] = pydantic.Field(
        default=None
    )
    """
    If this category sorts items in a nonstandard way, this will be the way we sort.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
