

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .approve_response_data_persistence import ApproveResponseDataPersistence
from .approve_response_data_status import ApproveResponseDataStatus


class ApproveResponseData(UniversalBaseModel):
    id: str
    status: ApproveResponseDataStatus
    persistence: ApproveResponseDataPersistence
    approved_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
