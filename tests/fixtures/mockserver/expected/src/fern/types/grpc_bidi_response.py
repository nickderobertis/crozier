

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .delay import Delay
from .grpc_bidi_response_rules_item import GrpcBidiResponseRulesItem
from .grpc_message import GrpcMessage
from .key_to_multi_value import KeyToMultiValue


class GrpcBidiResponse(UniversalBaseModel):
    """
    gRPC bidi response for bidirectional streaming
    """

    delay: typing.Optional[Delay] = None
    headers: typing.Optional[KeyToMultiValue] = None
    status_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="statusName"), pydantic.Field(alias="statusName")
    ] = None
    status_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="statusMessage"), pydantic.Field(alias="statusMessage")
    ] = None
    messages: typing.Optional[typing.List[GrpcMessage]] = None
    rules: typing.Optional[typing.List[GrpcBidiResponseRulesItem]] = None
    close_connection: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="closeConnection"), pydantic.Field(alias="closeConnection")
    ] = None
    primary: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GrpcBidiResponse)
