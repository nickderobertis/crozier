

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_binding_remove_property import (
    TransactionRequestOperationsOperationsItemActionDeformerBindingRemoveProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerBindingRemove(UniversalBaseModel):
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionDeformerBindingRemoveProperty

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
