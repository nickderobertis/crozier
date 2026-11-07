

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .common_response_status import CommonResponseStatus
from .common_task_ticket import CommonTaskTicket


class TicketGetTaskResponse(UniversalBaseModel):
    status: CommonResponseStatus
    result: CommonTaskTicket

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
