

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_transform_operator import (
    TransactionRequestOperationsOperationsItemActionDeformerTransformOperator,
)
from .transaction_request_operations_operations_item_action_deformer_transform_property import (
    TransactionRequestOperationsOperationsItemActionDeformerTransformProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerTransform(UniversalBaseModel):
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    property: TransactionRequestOperationsOperationsItemActionDeformerTransformProperty
    operator: TransactionRequestOperationsOperationsItemActionDeformerTransformOperator
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
