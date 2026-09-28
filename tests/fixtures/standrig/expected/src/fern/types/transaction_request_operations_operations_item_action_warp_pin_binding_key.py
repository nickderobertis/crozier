

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_warp_pin_binding_key_curve import (
    TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurve,
)
from .transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_warp_pin_binding_key_property import (
    TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyProperty,
)


class TransactionRequestOperationsOperationsItemActionWarpPinBindingKey(UniversalBaseModel):
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    pin_id: typing_extensions.Annotated[str, FieldMetadata(alias="pinId"), pydantic.Field(alias="pinId")]
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolation] = (
        None
    )
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
