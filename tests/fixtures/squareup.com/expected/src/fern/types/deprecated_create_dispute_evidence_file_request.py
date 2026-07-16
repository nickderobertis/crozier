

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeprecatedCreateDisputeEvidenceFileRequest(UniversalBaseModel):
    """
    Defines the parameters for a `DeprecatedCreateDisputeEvidenceFile` request.
    """

    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MIME type of the uploaded file.
    The type can be image/heic, image/heif, image/jpeg, application/pdf, image/png, or image/tiff.
    """

    evidence_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of evidence you are uploading.
    """

    idempotency_key: str = pydantic.Field()
    """
    The Unique ID. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
