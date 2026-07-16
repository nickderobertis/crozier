

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class Destiny2TransferItemResponse(UniversalBaseModel):
    detailed_error_trace: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="DetailedErrorTrace"), pydantic.Field(alias="DetailedErrorTrace")
    ] = None
    error_code: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ErrorCode"), pydantic.Field(alias="ErrorCode")
    ] = None
    error_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ErrorStatus"), pydantic.Field(alias="ErrorStatus")
    ] = None
    message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Message"), pydantic.Field(alias="Message")
    ] = None
    message_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="MessageData"), pydantic.Field(alias="MessageData")
    ] = None
    response: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="Response"), pydantic.Field(alias="Response")
    ] = None
    throttle_seconds: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ThrottleSeconds"), pydantic.Field(alias="ThrottleSeconds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
