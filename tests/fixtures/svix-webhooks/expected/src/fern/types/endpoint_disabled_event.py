

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_disabled_event_data import EndpointDisabledEventData
from .endpoint_disabled_event_type import EndpointDisabledEventType


class EndpointDisabledEvent(UniversalBaseModel):
    """
    Sent when an endpoint has been automatically disabled after continuous failures.
    """

    data: EndpointDisabledEventData
    type: EndpointDisabledEventType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
