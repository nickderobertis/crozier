

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ArtifactFormat(UniversalBaseModel):
    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None
    file_extension: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fileExtension"), pydantic.Field(alias="fileExtension")
    ] = None
    for_content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="forContentType"), pydantic.Field(alias="forContentType")
    ] = None
    label: typing.Optional[str] = None
    preserve_aspect_ratio: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="preserveAspectRatio"), pydantic.Field(alias="preserveAspectRatio")
    ] = None
    public: typing.Optional[bool] = None
    upscale_allowed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="upscaleAllowed"), pydantic.Field(alias="upscaleAllowed")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
