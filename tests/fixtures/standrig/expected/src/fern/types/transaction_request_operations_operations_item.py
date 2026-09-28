

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action import TransactionRequestOperationsOperationsItemAction
from .transaction_request_operations_operations_item_target import TransactionRequestOperationsOperationsItemTarget


class TransactionRequestOperationsOperationsItem(UniversalBaseModel):
    id: str
    name: str
    enabled: typing.Optional[bool] = None
    target: TransactionRequestOperationsOperationsItemTarget
    action: TransactionRequestOperationsOperationsItemAction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
