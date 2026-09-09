

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_create400details_item_a_required_field_is_missing_issue import (
    ProductsCreate400DetailsItemARequiredFieldIsMissingIssue,
)


class ProductsCreate400DetailsItemARequiredFieldIsMissing(UniversalBaseModel):
    issue: typing.Optional[ProductsCreate400DetailsItemARequiredFieldIsMissingIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
