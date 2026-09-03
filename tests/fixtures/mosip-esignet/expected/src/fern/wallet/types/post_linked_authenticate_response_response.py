

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostLinkedAuthenticateResponseResponse(UniversalBaseModel):
    linked_transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="linkedTransactionId"),
        pydantic.Field(
            alias="linkedTransactionId",
            description="This is the same transactionId sent in the oauth-details response.",
        ),
    ] = None
    """
    This is the same transactionId sent in the oauth-details response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
