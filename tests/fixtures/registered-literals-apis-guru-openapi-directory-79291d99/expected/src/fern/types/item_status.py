

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_status_investments import ItemStatusInvestments
from .item_status_last_webhook import ItemStatusLastWebhook
from .item_status_transactions import ItemStatusTransactions


class ItemStatus(UniversalBaseModel):
    """
    An object with information about the status of the Item.
    """

    investments: typing.Optional[ItemStatusInvestments] = None
    last_webhook: typing.Optional[ItemStatusLastWebhook] = None
    transactions: typing.Optional[ItemStatusTransactions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
