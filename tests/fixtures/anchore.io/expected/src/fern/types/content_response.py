

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentResponse(UniversalBaseModel):
    """
    Generic wrapper for content listings from images
    """

    content: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    content_type: typing.Optional[str] = None
    image_digest: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageDigest"), pydantic.Field(alias="imageDigest")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
