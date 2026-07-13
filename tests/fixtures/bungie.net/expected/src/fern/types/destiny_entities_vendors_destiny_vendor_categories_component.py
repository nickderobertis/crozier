

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_entities_vendors_destiny_vendor_category import DestinyEntitiesVendorsDestinyVendorCategory


class DestinyEntitiesVendorsDestinyVendorCategoriesComponent(UniversalBaseModel):
    """
    A vendor can have many categories of items that they sell. This component will return the category information for available items, as well as the index into those items in the user's sale item list.
    Note that, since both the category and items are indexes, this data is Content Version dependent. Be sure to check that your content is up to date before using this data. This is an unfortunate, but permanent, limitation of Vendor data.
    """

    categories: typing.Optional[typing.List[DestinyEntitiesVendorsDestinyVendorCategory]] = pydantic.Field(default=None)
    """
    The list of categories for items that the vendor sells, in rendering order.
    These categories each point to a "display category" in the displayCategories property of the DestinyVendorDefinition, as opposed to the other categories.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
