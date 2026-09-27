

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_with_content_type_base64bytes_type import BodyWithContentTypeBase64BytesType


class BodyWithContentTypeBase64Bytes(UniversalBaseModel):
    """
    binary response body
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    type: typing.Optional[BodyWithContentTypeBase64BytesType] = None
    base64bytes: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="base64Bytes"), pydantic.Field(alias="base64Bytes")
    ] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None
    optional: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
