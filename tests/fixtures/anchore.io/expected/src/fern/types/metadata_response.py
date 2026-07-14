

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MetadataResponse(UniversalBaseModel):
    """
    Generic wrapper for metadata listings from images
    """

    image_digest: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="imageDigest")] = None
    metadata: typing.Optional[typing.Optional[typing.Any]] = None
    metadata_type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
