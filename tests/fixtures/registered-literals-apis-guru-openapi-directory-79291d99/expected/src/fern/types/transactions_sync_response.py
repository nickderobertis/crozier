

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .removed_transaction import RemovedTransaction
from .request_id import RequestId
from .transaction import Transaction


class TransactionsSyncResponse(UniversalBaseModel):
    """
    TransactionsSyncResponse defines the response schema for `/transactions/sync`
    """

    added: typing.List[Transaction] = pydantic.Field()
    """
    Transactions that have been added to the Item since `cursor` ordered by ascending last modified time.
    """

    has_more: bool = pydantic.Field()
    """
    Represents if more than requested count of transaction updates exist. If true, the additional updates can be fetched by making an additional request with `cursor` set to `next_cursor`. If `has_more` is true, it’s important to pull all available pages, to make it less likely for underlying data changes to conflict with pagination.
    """

    modified: typing.List[Transaction] = pydantic.Field()
    """
    Transactions that have been modified on the Item since `cursor` ordered by ascending last modified time.
    """

    next_cursor: str = pydantic.Field()
    """
    Cursor used for fetching any future updates after the latest update provided in this response. The cursor obtained after all pages have been pulled (indicated by `has_more` being `false`) will be valid for at least 1 year. This cursor should be persisted for later calls. If transactions are not yet available, this will be an empty string.
    """

    removed: typing.List[RemovedTransaction] = pydantic.Field()
    """
    Transactions that have been removed from the Item since `cursor` ordered by ascending last modified time.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
