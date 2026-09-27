

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_binding_key_curve import (
    TransactionRequestOperationsOperationsItemActionBindingKeyCurve,
)
from .transaction_request_operations_operations_item_action_binding_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionBindingKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_binding_key_property import (
    TransactionRequestOperationsOperationsItemActionBindingKeyProperty,
)


class TransactionRequestOperationsOperationsItemActionBindingKey(UniversalBaseModel):
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionBindingKeyInterpolation] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
