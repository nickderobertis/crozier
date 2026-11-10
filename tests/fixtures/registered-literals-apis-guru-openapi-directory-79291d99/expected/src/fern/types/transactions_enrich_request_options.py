

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransactionsEnrichRequestOptions(UniversalBaseModel):
    """
    An optional object to be used with the request.
    """

    include_legacy_category: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include `legacy_category` and `legacy_category_id` in the response (in addition to the default `personal_finance_category`).
    
    Categories are based on Plaid's legacy taxonomy. For a full list of legacy categories, see [`/categories/get`](https://plaid.com/docs/api/products/transactions/#categoriesget).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
