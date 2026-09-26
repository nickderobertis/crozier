

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .model_preprocess_config_image_quality import ModelPreprocessConfigImageQuality


class ModelPreprocessConfig(UniversalBaseModel):
    trim_margins: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="trimMargins"), pydantic.Field(alias="trimMargins")
    ] = None
    use_ghost_script: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="useGhostScript"), pydantic.Field(alias="useGhostScript")
    ] = None
    start_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="startPage"), pydantic.Field(alias="startPage")
    ] = None
    pages: typing.Optional[typing.List[int]] = None
    use_poppler: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="usePoppler"), pydantic.Field(alias="usePoppler")
    ] = None
    pad_to_fit: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="padToFit"), pydantic.Field(alias="padToFit")
    ] = None
    use_text_detection: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="useTextDetection"), pydantic.Field(alias="useTextDetection")
    ] = None
    max_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxPages"), pydantic.Field(alias="maxPages")
    ] = None
    rotation: typing.Optional[int] = None
    deskew_image: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="deskewImage"), pydantic.Field(alias="deskewImage")
    ] = None
    auto_rotate: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="autoRotate"), pydantic.Field(alias="autoRotate")
    ] = None
    image_quality: typing_extensions.Annotated[
        typing.Optional[ModelPreprocessConfigImageQuality],
        FieldMetadata(alias="imageQuality"),
        pydantic.Field(alias="imageQuality"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
