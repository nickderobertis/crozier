

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_count_allocation import RequestCountAllocation


class ConsumerRequestCountsInDateRangeResponseData(UniversalBaseModel):
    aggregated_request_count: typing.Optional[float] = None
    application_id: typing.Optional[str] = None
    consumer_id: typing.Optional[str] = None
    end_datetime: typing.Optional[str] = None
    request_counts: typing.Optional[RequestCountAllocation] = None
    start_datetime: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
