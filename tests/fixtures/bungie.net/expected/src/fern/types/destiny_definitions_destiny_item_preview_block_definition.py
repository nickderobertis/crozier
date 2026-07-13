

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_items_destiny_derived_item_category_definition import (
    DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition,
)


class DestinyDefinitionsDestinyItemPreviewBlockDefinition(UniversalBaseModel):
    """
    Items like Sacks or Boxes can have items that it shows in-game when you view details that represent the items you can obtain if you use or acquire the item.
    This defines those categories, and gives some insights into that data's source.
    """

    artifact_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="artifactHash")] = (
        pydantic.Field(default=None)
    )
    """
    If this item should show you Artifact information when you preview it, this is the hash identifier of the DestinyArtifactDefinition for the artifact whose data should be shown.
    """

    derived_item_categories: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition]],
        FieldMetadata(alias="derivedItemCategories"),
    ] = pydantic.Field(default=None)
    """
    This is a list of the items being previewed, categorized in the same way as they are in the preview UI.
    """

    preview_action_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="previewActionString")
    ] = pydantic.Field(default=None)
    """
    If the preview has an associated action (like "Open"), this will be the localized string for that action.
    """

    preview_vendor_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="previewVendorHash")] = (
        pydantic.Field(default=None)
    )
    """
    If the preview data is derived from a fake "Preview" Vendor, this will be the hash identifier for the DestinyVendorDefinition of that fake vendor.
    """

    screen_style: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="screenStyle")] = (
        pydantic.Field(default=None)
    )
    """
    A string that the game UI uses as a hint for which detail screen to show for the item. You, too, can leverage this for your own custom screen detail views. Note, however, that these are arbitrarily defined by designers: there's no guarantees of a fixed, known number of these - so fall back to something reasonable if you don't recognize it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
