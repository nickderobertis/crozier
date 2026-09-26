

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_mcp_browser_open_failed_properties import EventMcpBrowserOpenFailedProperties


class EventMcpBrowserOpenFailed(UniversalBaseModel):
    properties: EventMcpBrowserOpenFailedProperties

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
