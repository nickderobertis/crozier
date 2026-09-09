

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_create400details_item_the_value_of_a_field_does_not_conform_to_the_expected_format_issue import (
    ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormatIssue,
)


class ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormat(UniversalBaseModel):
    issue: typing.Optional[ProductsCreate400DetailsItemTheValueOfAFieldDoesNotConformToTheExpectedFormatIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
