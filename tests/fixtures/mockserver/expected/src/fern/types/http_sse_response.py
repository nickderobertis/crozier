

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay
from .http_sse_response_events_item import HttpSseResponseEventsItem
from .key_to_multi_value import KeyToMultiValue


class HttpSseResponse(UniversalBaseModel):
    """
    SSE response to return
    """

    delay: typing.Optional[Delay] = None
    headers: typing.Optional[KeyToMultiValue] = None
    status_code: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="statusCode"), pydantic.Field(alias="statusCode")
    ] = None
    events: typing.Optional[typing.List[HttpSseResponseEventsItem]] = None
    close_connection: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="closeConnection"), pydantic.Field(alias="closeConnection")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
