

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_id import CellId
from .marimo_exception_raised_error_type import MarimoExceptionRaisedErrorType


class MarimoExceptionRaisedError(UniversalBaseModel):
    exception_type: str
    msg: str
    raising_cell: typing.Optional[CellId] = None
    traceback: typing.Optional[str] = None
    type: MarimoExceptionRaisedErrorType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
