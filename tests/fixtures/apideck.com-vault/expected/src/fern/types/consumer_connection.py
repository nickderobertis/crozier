

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .auth_type import AuthType
from .consumer_connection_state import ConsumerConnectionState


class ConsumerConnection(UniversalBaseModel):
    auth_type: typing.Optional[AuthType] = None
    consumer_id: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    icon: typing.Optional[str] = None
    id: typing.Optional[str] = None
    logo: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Attach your own consumer specific metadata
    """

    name: typing.Optional[str] = None
    service_id: typing.Optional[str] = None
    settings: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Connection settings. Values will persist to `form_fields` with corresponding id
    """

    state: typing.Optional[ConsumerConnectionState] = None
    tag_line: typing.Optional[str] = None
    unified_api: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
