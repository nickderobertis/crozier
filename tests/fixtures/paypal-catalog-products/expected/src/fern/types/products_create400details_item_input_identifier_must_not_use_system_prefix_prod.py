

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products_create400details_item_input_identifier_must_not_use_system_prefix_prod_issue import (
    ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue,
)


class ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProd(UniversalBaseModel):
    issue: typing.Optional[ProductsCreate400DetailsItemInputIdentifierMustNotUseSystemPrefixProdIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
