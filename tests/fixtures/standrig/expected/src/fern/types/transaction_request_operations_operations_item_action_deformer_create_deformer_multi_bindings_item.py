

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_composition import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemComposition,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCurve,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_keyforms_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemKeyformsItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItem(UniversalBaseModel):
    parameters: typing.List[typing.Any]
    composition: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemComposition
    ] = None
    property: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemProperty
    keyforms: typing.List[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemKeyformsItem
    ]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolation
    ] = None
    curve: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCurve
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
