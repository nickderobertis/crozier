

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_artmesh_binding_key_curve import ModelingOperationActionArtmeshBindingKeyCurve
from .modeling_operation_action_artmesh_binding_key_interpolation import (
    ModelingOperationActionArtmeshBindingKeyInterpolation,
)
from .modeling_operation_action_artmesh_binding_key_offsets_item import (
    ModelingOperationActionArtmeshBindingKeyOffsetsItem,
)


class ModelingOperationActionArtmeshBindingKey(UniversalBaseModel):
    parameter: str
    input: float
    offsets: typing.List[ModelingOperationActionArtmeshBindingKeyOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionArtmeshBindingKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionArtmeshBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
