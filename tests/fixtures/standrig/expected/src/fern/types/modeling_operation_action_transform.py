

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_transform_operator import ModelingOperationActionTransformOperator
from .modeling_operation_action_transform_property import ModelingOperationActionTransformProperty


class ModelingOperationActionTransform(UniversalBaseModel):
    property: ModelingOperationActionTransformProperty
    operator: ModelingOperationActionTransformOperator
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
