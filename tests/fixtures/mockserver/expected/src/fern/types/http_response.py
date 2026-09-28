

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .body_with_content_type import BodyWithContentType
from .connection_options import ConnectionOptions
from .delay import Delay
from .key_to_multi_value import KeyToMultiValue
from .key_to_value import KeyToValue


class HttpResponse(UniversalBaseModel):
    """
    response to return
    """

    delay: typing.Optional[Delay] = None
    body: typing.Optional[BodyWithContentType] = None
    cookies: typing.Optional[KeyToValue] = None
    connection_options: typing_extensions.Annotated[
        typing.Optional[ConnectionOptions],
        FieldMetadata(alias="connectionOptions"),
        pydantic.Field(alias="connectionOptions"),
    ] = None
    headers: typing.Optional[KeyToMultiValue] = None
    trailers: typing.Optional[KeyToMultiValue] = None
    status_code: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="statusCode"), pydantic.Field(alias="statusCode")
    ] = None
    reason_phrase: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="reasonPhrase"), pydantic.Field(alias="reasonPhrase")
    ] = None
    recover_after: typing_extensions.Annotated[
        typing.Optional["RecoverAfter"], FieldMetadata(alias="recoverAfter"), pydantic.Field(alias="recoverAfter")
    ] = None
    status_code_range: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="statusCodeRange"), pydantic.Field(alias="statusCodeRange")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .recover_after import RecoverAfter

update_forward_refs(HttpResponse, RecoverAfter=RecoverAfter)
