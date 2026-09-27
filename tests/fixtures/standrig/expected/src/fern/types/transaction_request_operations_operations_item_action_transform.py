

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_transform_operator import (
    TransactionRequestOperationsOperationsItemActionTransformOperator,
)
from .transaction_request_operations_operations_item_action_transform_property import (
    TransactionRequestOperationsOperationsItemActionTransformProperty,
)


class TransactionRequestOperationsOperationsItemActionTransform(UniversalBaseModel):
    property: TransactionRequestOperationsOperationsItemActionTransformProperty
    operator: TransactionRequestOperationsOperationsItemActionTransformOperator
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
