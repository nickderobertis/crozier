

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_id import CellId
from .marimo_strict_execution_error_type import MarimoStrictExecutionErrorType


class MarimoStrictExecutionError(UniversalBaseModel):
    blamed_cell: typing.Optional[CellId] = None
    msg: str
    ref: str
    type: MarimoStrictExecutionErrorType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
