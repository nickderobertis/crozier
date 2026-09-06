

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_action_http_config_method import EventActionHttpConfigMethod
from .http_part import HttpPart
from .key_value import KeyValue
from .secret import Secret


class EventActionHttpConfig(UniversalBaseModel):
    endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTP endpoint
    """

    username: typing.Optional[str] = None
    password: typing.Optional[Secret] = None
    headers: typing.Optional[typing.List[KeyValue]] = pydantic.Field(default=None)
    """
    headers to add
    """

    timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    Ignored for multipart requests with files as attachments
    """

    skip_tls_verify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if enabled the HTTP client accepts any TLS certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks. This should be used only for testing.
    """

    method: typing.Optional[EventActionHttpConfigMethod] = None
    query_parameters: typing.Optional[typing.List[KeyValue]] = None
    body: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTP POST/PUT body
    """

    parts: typing.Optional[typing.List[HttpPart]] = pydantic.Field(default=None)
    """
    Multipart requests allow to combine one or more sets of data into a single body. For each part, you can set a file path or a body as text. Placeholders are supported in file path, body, header values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
