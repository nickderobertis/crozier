

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .content_package_response_content_item import ContentPackageResponseContentItem


class ContentPackageResponse(UniversalBaseModel):
    """
    Package content listings from images
    """

    content: typing.Optional[typing.List[ContentPackageResponseContentItem]] = None
    content_type: typing.Optional[str] = None
    image_digest: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="imageDigest")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
