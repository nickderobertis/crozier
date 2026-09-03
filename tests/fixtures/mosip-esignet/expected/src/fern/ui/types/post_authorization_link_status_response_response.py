

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_authorization_link_status_response_response_link_status import (
    PostAuthorizationLinkStatusResponseResponseLinkStatus,
)


class PostAuthorizationLinkStatusResponseResponse(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionId"),
        pydantic.Field(alias="transactionId", description="This is the same transactionId as sent in the request."),
    ] = None
    """
    This is the same transactionId as sent in the request.
    """

    link_status: typing_extensions.Annotated[
        typing.Optional[PostAuthorizationLinkStatusResponseResponseLinkStatus],
        FieldMetadata(alias="linkStatus"),
        pydantic.Field(alias="linkStatus", description="Link status of the linkCode passed in the request."),
    ] = None
    """
    Link status of the linkCode passed in the request.
    """

    linked_date_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="linkedDateTime"),
        pydantic.Field(
            alias="linkedDateTime",
            description="Epoch in milliseconds at which the wallet-app acknowledged the link-code.",
        ),
    ] = None
    """
    Epoch in milliseconds at which the wallet-app acknowledged the link-code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
