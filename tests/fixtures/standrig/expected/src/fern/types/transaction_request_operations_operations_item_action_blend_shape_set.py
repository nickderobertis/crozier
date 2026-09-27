

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_blend_shape_set_shape import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShape,
)


class TransactionRequestOperationsOperationsItemActionBlendShapeSet(UniversalBaseModel):
    shape: TransactionRequestOperationsOperationsItemActionBlendShapeSetShape

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
