

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .send_category_mapping_to_vtex_mapper_categories_item_children_item import (
    SendCategoryMappingToVtexMapperCategoriesItemChildrenItem,
)


class SendCategoryMappingToVtexMapperCategoriesItem(UniversalBaseModel):
    children: typing.Optional[typing.List[SendCategoryMappingToVtexMapperCategoriesItemChildrenItem]] = pydantic.Field(
        default=None
    )
    """
    Array with children categories in the marketplace, and their information.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the parent category in the marketplace.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the parent category in the marketplace.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
