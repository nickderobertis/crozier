

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_categories_response_category_list_categories_item import ListCategoriesResponseCategoryListCategoriesItem


class ListCategoriesResponseCategoryList(UniversalBaseModel):
    can_create_category: bool
    can_create_topic: bool
    categories: typing.List[ListCategoriesResponseCategoryListCategoriesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
