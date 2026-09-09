

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_create400details_item_the_value_of_a_field_is_invalid_issue import (
    ProductsCreate400DetailsItemTheValueOfAFieldIsInvalidIssue,
)


class ProductsCreate400DetailsItemTheValueOfAFieldIsInvalid(UniversalBaseModel):
    issue: typing.Optional[ProductsCreate400DetailsItemTheValueOfAFieldIsInvalidIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
