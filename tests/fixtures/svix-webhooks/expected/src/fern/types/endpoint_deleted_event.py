

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_deleted_event_data import EndpointDeletedEventData
from .endpoint_deleted_event_type import EndpointDeletedEventType


class EndpointDeletedEvent(UniversalBaseModel):
    """
    Sent when an endpoint is deleted.
    """

    data: EndpointDeletedEventData
    type: EndpointDeletedEventType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
