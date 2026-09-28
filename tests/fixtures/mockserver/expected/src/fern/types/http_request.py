

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .jwt import Jwt
from .key_to_multi_value import KeyToMultiValue
from .key_to_value import KeyToValue
from .protocol import Protocol
from .socket_address import SocketAddress
from .string_or_json_schema import StringOrJsonSchema


class HttpRequest(UniversalBaseModel):
    """
    request properties matcher
    """

    secure: typing.Optional[bool] = None
    keep_alive: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="keepAlive"), pydantic.Field(alias="keepAlive")
    ] = None
    method: typing.Optional[StringOrJsonSchema] = None
    path: typing.Optional[StringOrJsonSchema] = None
    path_parameters: typing_extensions.Annotated[
        typing.Optional[KeyToMultiValue], FieldMetadata(alias="pathParameters"), pydantic.Field(alias="pathParameters")
    ] = None
    query_string_parameters: typing_extensions.Annotated[
        typing.Optional[KeyToMultiValue],
        FieldMetadata(alias="queryStringParameters"),
        pydantic.Field(alias="queryStringParameters"),
    ] = None
    body: typing.Optional["Body"] = None
    headers: typing.Optional[KeyToMultiValue] = None
    cookies: typing.Optional[KeyToValue] = None
    socket_address: typing_extensions.Annotated[
        typing.Optional[SocketAddress], FieldMetadata(alias="socketAddress"), pydantic.Field(alias="socketAddress")
    ] = None
    protocol: typing.Optional[Protocol] = None
    jwt: typing.Optional[Jwt] = None
    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    respond_before_body: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="respondBeforeBody"),
        pydantic.Field(
            alias="respondBeforeBody",
            description="If true, MockServer responds to a matching request before consuming its body and may close the connection. Required: the matcher must not specify a body matcher, and the action must be RESPONSE or ERROR.",
        ),
    ] = None
    """
    If true, MockServer responds to a matching request before consuming its body and may close the connection. Required: the matcher must not specify a body matcher, and the action must be RESPONSE or ERROR.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .body import Body
from .body_body_all_of import BodyBodyAllOf

update_forward_refs(HttpRequest, Body=Body, BodyBodyAllOf=BodyBodyAllOf)
