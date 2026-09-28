

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .grpc_message import GrpcMessage
from .string_or_json_schema import StringOrJsonSchema


class GrpcBidiResponseRulesItem(UniversalBaseModel):
    match_json: typing_extensions.Annotated[
        typing.Optional[StringOrJsonSchema], FieldMetadata(alias="matchJson"), pydantic.Field(alias="matchJson")
    ] = None
    responses: typing.Optional[typing.List[GrpcMessage]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GrpcBidiResponseRulesItem)
