

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_with_content_type_content_type_template_type import BodyWithContentTypeContentTypeTemplateType
from .body_with_content_type_content_type_type import BodyWithContentTypeContentTypeType


class BodyWithContentTypeContentType(UniversalBaseModel):
    """
    file response body — served from a file, optionally rendered as a template against the request
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    type: typing.Optional[BodyWithContentTypeContentTypeType] = None
    file_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="filePath"), pydantic.Field(alias="filePath")
    ] = None
    template_type: typing_extensions.Annotated[
        typing.Optional[BodyWithContentTypeContentTypeTemplateType],
        FieldMetadata(alias="templateType"),
        pydantic.Field(alias="templateType"),
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
