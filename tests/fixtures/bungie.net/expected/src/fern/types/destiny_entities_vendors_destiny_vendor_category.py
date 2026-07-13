

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyEntitiesVendorsDestinyVendorCategory(UniversalBaseModel):
    """
    Information about the category and items currently sold in that category.
    """

    display_category_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="displayCategoryIndex")
    ] = pydantic.Field(default=None)
    """
    An index into the DestinyVendorDefinition.displayCategories property, so you can grab the display data for this category.
    """

    item_indexes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="itemIndexes")] = (
        pydantic.Field(default=None)
    )
    """
    An ordered list of indexes into items being sold in this category (DestinyVendorDefinition.itemList) which will contain more information about the items being sold themselves. Can also be used to index into DestinyVendorSaleItemComponent data, if you asked for that data to be returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
