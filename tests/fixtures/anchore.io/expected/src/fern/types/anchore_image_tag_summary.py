

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AnchoreImageTagSummary(UniversalBaseModel):
    """
    A unique image in the engine.
    """

    analysis_status: typing.Optional[str] = None
    analyzed_at: typing.Optional[int] = None
    created_at: typing.Optional[int] = None
    fulltag: typing.Optional[str] = None
    image_digest: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageDigest"), pydantic.Field(alias="imageDigest")
    ] = None
    image_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageId"), pydantic.Field(alias="imageId")
    ] = None
    image_status: typing.Optional[str] = None
    parent_digest: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentDigest"), pydantic.Field(alias="parentDigest")
    ] = None
    tag_detected_at: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
