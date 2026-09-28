

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItem(UniversalBaseModel):
    id: str
    name: str
    enabled: bool
    u: float
    v: float
    offset_x: typing_extensions.Annotated[float, FieldMetadata(alias="offsetX"), pydantic.Field(alias="offsetX")]
    offset_y: typing_extensions.Annotated[float, FieldMetadata(alias="offsetY"), pydantic.Field(alias="offsetY")]
    radius: float
    strength: float
    linked_mirror_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="linkedMirrorId"), pydantic.Field(alias="linkedMirrorId")
    ] = None
    bindings: typing.Optional[
        typing.List[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItem]
    ] = None
    multi_bindings: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem
            ]
        ],
        FieldMetadata(alias="multiBindings"),
        pydantic.Field(alias="multiBindings"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
