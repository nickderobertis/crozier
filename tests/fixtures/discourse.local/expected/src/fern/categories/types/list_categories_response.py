

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_categories_response_category_list import ListCategoriesResponseCategoryList


class ListCategoriesResponse(UniversalBaseModel):
    category_list: ListCategoriesResponseCategoryList

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
