

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransactionsGetRequestOptions(UniversalBaseModel):
    """
    An optional object to be used with the request. If specified, `options` must not be `null`.
    """

    account_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of `account_ids` to retrieve for the Item
    
    Note: An error will be returned if a provided `account_id` is not associated with the Item.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of transactions to fetch.
    """

    include_logo_and_counterparty_beta: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include counterparties and extran merchant fields in the transaction. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager.
    """

    include_original_description: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager, or submit a [Support request](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/product-functionality) .
    """

    include_personal_finance_category: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include the [`personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-personal-finance-category) object in the response.
    
    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    
    We’re introducing Category Rules - a new beta endpoint that will enable you to change the `personal_finance_category` for a transaction based on your users’ needs. When rules are set, the selected category will override the Plaid provided category. To learn more, send a note to transactions-feedback@plaid.com.
    """

    include_personal_finance_category_beta: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Please use [`include_personal_finance_category`](https://plaid.com/docs/api/products/transactions/#transactions-get-request-options-include-personal-finance-category) instead.
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of transactions to skip. The default value is 0.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
