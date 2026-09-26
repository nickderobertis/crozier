

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2UploadPartUrl(UniversalBaseModel):
    """
    A signed URL and required headers for one multipart upload part.
    """

    part_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="partNumber"), pydantic.Field(alias="partNumber", description="Multipart part number.")
    ]
    """
    Multipart part number.
    """

    url: str = pydantic.Field()
    """
    Signed URL for this upload part. Upload bytes with `PUT` and exactly the supplied headers; never construct or modify the signed URL. Treat any `2xx` as success. Sim-hosted URLs return an empty `204` and v2 JSON errors. Object-storage URLs may return `200` or `201` and provider-specific errors, often XML. Do not retain part `ETag` values; after every part succeeds, call the completion endpoint without a request body.
    """

    headers: typing.Dict[str, str] = pydantic.Field()
    """
    Headers that must be included with the part upload.
    """

    expires_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="ISO 8601 expiration time for the signed URL."),
    ]
    """
    ISO 8601 expiration time for the signed URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
