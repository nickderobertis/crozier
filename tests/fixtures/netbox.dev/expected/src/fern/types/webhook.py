

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_http_method import WebhookHttpMethod


class Webhook(UniversalBaseModel):
    additional_headers: typing.Optional[str] = pydantic.Field(default=None)
    """
    User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).
    """

    body_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.
    """

    ca_file_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.
    """

    conditions: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    A set of conditions which determine whether the webhook will be generated.
    """

    content_types: typing.List[str]
    created: typing.Optional[dt.datetime] = None
    display: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    http_content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.
    """

    http_method: typing.Optional[WebhookHttpMethod] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    payload_url: str = pydantic.Field()
    """
    This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.
    """

    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.
    """

    ssl_verification: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable SSL certificate verification. Disable with caution!
    """

    type_create: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Call this webhook when a matching object is created.
    """

    type_delete: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Call this webhook when a matching object is deleted.
    """

    type_update: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Call this webhook when a matching object is updated.
    """

    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
