

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_updated_event_data import EndpointUpdatedEventData
from .endpoint_updated_event_type import EndpointUpdatedEventType


class EndpointUpdatedEvent(UniversalBaseModel):
    """
    Sent when an endpoint is updated.
    """

    data: EndpointUpdatedEventData
    type: EndpointUpdatedEventType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
