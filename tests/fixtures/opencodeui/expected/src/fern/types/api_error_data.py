

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiErrorData(UniversalBaseModel):
    message: str
    status_code: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="statusCode"), pydantic.Field(alias="statusCode")
    ] = None
    is_retryable: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isRetryable"), pydantic.Field(alias="isRetryable")
    ]
    response_headers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="responseHeaders"),
        pydantic.Field(alias="responseHeaders"),
    ] = None
    response_body: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseBody"), pydantic.Field(alias="responseBody")
    ] = None
    metadata: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
