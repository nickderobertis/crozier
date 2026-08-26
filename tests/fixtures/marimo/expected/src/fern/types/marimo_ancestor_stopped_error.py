

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_id import CellId
from .marimo_ancestor_stopped_error_type import MarimoAncestorStoppedErrorType


class MarimoAncestorStoppedError(UniversalBaseModel):
    msg: str
    raising_cell: CellId
    type: MarimoAncestorStoppedErrorType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
