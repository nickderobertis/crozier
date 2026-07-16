

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeprecatedCreateDisputeEvidenceTextRequest(UniversalBaseModel):
    """
    Defines the parameters for a `DeprecatedCreateDisputeEvidenceText` request.
    """

    evidence_text: str = pydantic.Field()
    """
    The evidence string.
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
