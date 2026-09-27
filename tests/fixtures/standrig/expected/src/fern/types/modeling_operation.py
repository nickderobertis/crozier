

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action import ModelingOperationAction
from .modeling_operation_target import ModelingOperationTarget


class ModelingOperation(UniversalBaseModel):
    id: str
    name: str
    enabled: typing.Optional[bool] = None
    target: ModelingOperationTarget
    action: ModelingOperationAction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
