

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_blend_shape_set_shape import ModelingOperationActionBlendShapeSetShape


class ModelingOperationActionBlendShapeSet(UniversalBaseModel):
    shape: ModelingOperationActionBlendShapeSetShape

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
