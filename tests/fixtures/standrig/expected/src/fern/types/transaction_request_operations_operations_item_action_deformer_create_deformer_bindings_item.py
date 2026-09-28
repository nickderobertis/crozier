

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_composition import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemComposition,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCurve,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_keys_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemKeysItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItem(UniversalBaseModel):
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemProperty
    keys: typing.List[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemKeysItem]
    additive: typing.Optional[bool] = None
    composition: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemComposition
    ] = None
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolation
    ] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCurve] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
