

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_response_auth_request import ConnectorResponseAuthRequest
from .connector_state import ConnectorState


class ConnectorResponse(UniversalBaseModel):
    id: str
    url: str
    state: ConnectorState
    auth_request: typing.Optional[ConnectorResponseAuthRequest] = None
    disconnect_reason: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    
    Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
    information about the object in a structured format, and querying for objects via API or the dashboard.
    
    Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
    512 characters.
    """

    created_at: dt.datetime
    updated_at: dt.datetime
    created_by: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
