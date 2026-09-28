

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_part_tint_tint_mode import (
    TransactionRequestOperationsOperationsItemActionPartTintTintMode,
)


class TransactionRequestOperationsOperationsItemActionPartTintTint(UniversalBaseModel):
    mode: TransactionRequestOperationsOperationsItemActionPartTintTintMode
    color: str
    opacity: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
