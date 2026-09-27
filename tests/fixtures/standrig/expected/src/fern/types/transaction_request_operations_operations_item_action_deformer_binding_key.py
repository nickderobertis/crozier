

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_binding_key_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurve,
)
from .transaction_request_operations_operations_item_action_deformer_binding_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_binding_key_property import (
    TransactionRequestOperationsOperationsItemActionDeformerBindingKeyProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerBindingKey(UniversalBaseModel):
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionDeformerBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolation] = (
        None
    )
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
