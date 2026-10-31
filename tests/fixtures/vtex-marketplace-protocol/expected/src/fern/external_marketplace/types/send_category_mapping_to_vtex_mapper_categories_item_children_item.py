

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .send_category_mapping_to_vtex_mapper_categories_item_children_item_specifications_item import (
    SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItem,
)


class SendCategoryMappingToVtexMapperCategoriesItemChildrenItem(UniversalBaseModel):
    children: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Grandchildren categories in the marketplace. Send as array of `ID`, `name` and `specifications`.
    """

    id: str = pydantic.Field()
    """
    ID of the child  category in the marketplace.
    """

    name: str = pydantic.Field()
    """
    Name of the child  category in the marketplace.
    """

    specifications: typing.List[SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItem] = (
        pydantic.Field()
    )
    """
    Specifications for the Product or SKU
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
