

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_artmesh_multi_key_curve import ModelingOperationActionArtmeshMultiKeyCurve
from .modeling_operation_action_artmesh_multi_key_interpolation import (
    ModelingOperationActionArtmeshMultiKeyInterpolation,
)
from .modeling_operation_action_artmesh_multi_key_offsets_item import ModelingOperationActionArtmeshMultiKeyOffsetsItem


class ModelingOperationActionArtmeshMultiKey(UniversalBaseModel):
    parameters: typing.List[typing.Any]
    inputs: typing.Dict[str, float]
    offsets: typing.List[ModelingOperationActionArtmeshMultiKeyOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionArtmeshMultiKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionArtmeshMultiKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
