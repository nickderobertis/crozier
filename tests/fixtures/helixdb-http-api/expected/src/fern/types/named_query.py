

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_condition import BatchCondition
from .operation_tree import OperationTree


class NamedQuery(UniversalBaseModel):
    name: typing.Optional[str] = None
    root: OperationTree
    condition: typing.Optional[BatchCondition] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
