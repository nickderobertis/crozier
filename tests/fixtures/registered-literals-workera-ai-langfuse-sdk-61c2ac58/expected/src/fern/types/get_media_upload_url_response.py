

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetMediaUploadUrlResponse(UniversalBaseModel):
    upload_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uploadUrl"),
        pydantic.Field(
            alias="uploadUrl",
            description="The presigned upload URL. If the asset is already uploaded, this will be null",
        ),
    ] = None
    """
    The presigned upload URL. If the asset is already uploaded, this will be null
    """

    media_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="mediaId"),
        pydantic.Field(alias="mediaId", description="The unique langfuse identifier of a media record"),
    ]
    """
    The unique langfuse identifier of a media record
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
