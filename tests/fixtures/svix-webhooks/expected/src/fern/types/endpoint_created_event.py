

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_created_event_data import EndpointCreatedEventData
from .endpoint_created_event_type import EndpointCreatedEventType


class EndpointCreatedEvent(UniversalBaseModel):
    """
    Sent when an endpoint is created.
    """

    data: EndpointCreatedEventData
    type: EndpointCreatedEventType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
