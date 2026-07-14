

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .anchore_image_analysis_status import AnchoreImageAnalysisStatus
from .anchore_image_image_status import AnchoreImageImageStatus
from .image_content import ImageContent
from .image_detail import ImageDetail


class AnchoreImage(UniversalBaseModel):
    """
    A unique image in the engine. May have multiple tags or references. Unique to an image content across registries or repositories.
    """

    analysis_status: typing.Optional[AnchoreImageAnalysisStatus] = pydantic.Field(default=None)
    """
    A state value for the current status of the analysis progress of the image
    """

    annotations: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    created_at: typing.Optional[dt.datetime] = None
    image_digest: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="imageDigest")] = None
    image_content: typing.Optional[ImageContent] = None
    image_detail: typing.Optional[typing.List[ImageDetail]] = pydantic.Field(default=None)
    """
    Details specific to an image reference and type such as tag and image source
    """

    image_status: typing.Optional[AnchoreImageImageStatus] = pydantic.Field(default=None)
    """
    State of the image
    """

    last_updated: typing.Optional[dt.datetime] = None
    record_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the record, used for internal schema updates and data migrations.
    """

    user_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="userId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
