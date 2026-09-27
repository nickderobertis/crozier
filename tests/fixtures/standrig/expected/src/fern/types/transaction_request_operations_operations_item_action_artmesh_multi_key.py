

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_artmesh_multi_key_curve import (
    TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurve,
)
from .transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_artmesh_multi_key_offsets_item import (
    TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyOffsetsItem,
)


class TransactionRequestOperationsOperationsItemActionArtmeshMultiKey(UniversalBaseModel):
    parameters: typing.List[typing.Any]
    inputs: typing.Dict[str, float]
    offsets: typing.List[TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolation] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
