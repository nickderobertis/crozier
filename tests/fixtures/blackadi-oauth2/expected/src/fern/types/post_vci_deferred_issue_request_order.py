

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PostVciDeferredIssueRequestOrder(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="transactionId"), pydantic.Field(alias="transactionId")
    ]
    credential_payload: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="credentialPayload"), pydantic.Field(alias="credentialPayload")
    ] = None
    credential_duration: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="credentialDuration"), pydantic.Field(alias="credentialDuration")
    ] = None
    signing_key_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signingKeyId"), pydantic.Field(alias="signingKeyId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
