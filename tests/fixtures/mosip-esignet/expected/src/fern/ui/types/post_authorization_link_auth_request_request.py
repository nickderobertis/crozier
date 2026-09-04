

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAuthorizationLinkAuthRequestRequest(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transactionId"),
        pydantic.Field(
            alias="transactionId", description="This is the same transactionId sent in the oauth-details response."
        ),
    ]
    """
    This is the same transactionId sent in the oauth-details response.
    """

    linked_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="linkedCode"), pydantic.Field(alias="linkedCode", description="LINKED linkCode.")
    ]
    """
    LINKED linkCode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
