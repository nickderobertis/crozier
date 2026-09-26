

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .operation_kind import OperationKind
from .operation_status import OperationStatus
from .operation_terminal import OperationTerminal


class Operation(UniversalBaseModel):
    created_at: dt.datetime
    finished_at: typing.Optional[dt.datetime] = None
    kind: OperationKind
    request_id: str
    started_at: typing.Optional[dt.datetime] = None
    status: OperationStatus
    terminal: typing.Optional[OperationTerminal] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
