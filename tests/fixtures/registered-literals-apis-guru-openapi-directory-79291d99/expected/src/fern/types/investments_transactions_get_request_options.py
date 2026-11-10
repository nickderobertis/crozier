

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvestmentsTransactionsGetRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/investments/transactions/get` results. If provided, must be non-`null`.
    """

    account_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of `account_ids` to retrieve for the Item.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of transactions to fetch.
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of transactions to skip when fetching transaction history
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
