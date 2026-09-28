

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PutMockserverGrpcServicesResponseItemMethodsItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    input_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputType"), pydantic.Field(alias="inputType")
    ] = None
    output_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="outputType"), pydantic.Field(alias="outputType")
    ] = None
    client_streaming: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="clientStreaming"), pydantic.Field(alias="clientStreaming")
    ] = None
    server_streaming: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="serverStreaming"), pydantic.Field(alias="serverStreaming")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
