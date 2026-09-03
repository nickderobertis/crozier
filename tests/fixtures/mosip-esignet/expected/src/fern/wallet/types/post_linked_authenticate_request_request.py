

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.auth_challenge import AuthChallenge


class PostLinkedAuthenticateRequestRequest(UniversalBaseModel):
    linked_transaction_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="linkedTransactionId"),
        pydantic.Field(
            alias="linkedTransactionId",
            description="This is the same transactionId sent in the link-transaction response.",
        ),
    ]
    """
    This is the same transactionId sent in the link-transaction response.
    """

    individual_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="individualId"),
        pydantic.Field(alias="individualId", description="User identifier (UIN/VID)."),
    ]
    """
    User identifier (UIN/VID).
    """

    challenge_list: typing_extensions.Annotated[
        typing.List[AuthChallenge],
        FieldMetadata(alias="challengeList"),
        pydantic.Field(alias="challengeList", description="Authentication Challenge."),
    ]
    """
    Authentication Challenge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
