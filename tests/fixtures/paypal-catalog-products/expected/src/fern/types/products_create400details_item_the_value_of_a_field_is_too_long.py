

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_create400details_item_the_value_of_a_field_is_too_long_issue import (
    ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue,
)


class ProductsCreate400DetailsItemTheValueOfAFieldIsTooLong(UniversalBaseModel):
    issue: typing.Optional[ProductsCreate400DetailsItemTheValueOfAFieldIsTooLongIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
