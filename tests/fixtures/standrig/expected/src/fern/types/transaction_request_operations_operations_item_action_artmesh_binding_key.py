

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_artmesh_binding_key_curve import (
    TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurve,
)
from .transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_artmesh_binding_key_offsets_item import (
    TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyOffsetsItem,
)


class TransactionRequestOperationsOperationsItemActionArtmeshBindingKey(UniversalBaseModel):
    parameter: str
    input: float
    offsets: typing.List[TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolation] = (
        None
    )
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
