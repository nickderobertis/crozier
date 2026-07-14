

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .consumer_connection import ConsumerConnection
from .consumer_id import ConsumerId
from .consumer_metadata import ConsumerMetadata
from .request_count_allocation import RequestCountAllocation


class Consumer(UniversalBaseModel):
    aggregated_request_count: typing.Optional[float] = None
    application_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of your Apideck Application
    """

    connections: typing.Optional[typing.List[ConsumerConnection]] = None
    consumer_id: ConsumerId
    created: typing.Optional[str] = None
    metadata: typing.Optional[ConsumerMetadata] = None
    modified: typing.Optional[str] = None
    request_count_updated: typing.Optional[str] = None
    request_counts: typing.Optional[RequestCountAllocation] = None
    services: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
