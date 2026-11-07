

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deny_response_data_persistence import DenyResponseDataPersistence
from .deny_response_data_status import DenyResponseDataStatus


class DenyResponseData(UniversalBaseModel):
    id: str
    status: DenyResponseDataStatus
    persistence: typing.Optional[DenyResponseDataPersistence] = None
    denied_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
