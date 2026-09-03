

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_send_linked_otp_request_request_otp_channels_item import PostSendLinkedOtpRequestRequestOtpChannelsItem


class PostSendLinkedOtpRequestRequest(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transactionId"),
        pydantic.Field(alias="transactionId", description="oauth-details transactionId is used until the /token call."),
    ]
    """
    oauth-details transactionId is used until the /token call.
    """

    individual_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="individualId"),
        pydantic.Field(alias="individualId", description="Actual UIN or VID value of the authenticating the end user."),
    ]
    """
    Actual UIN or VID value of the authenticating the end user.
    """

    otp_channels: typing_extensions.Annotated[
        typing.List[PostSendLinkedOtpRequestRequestOtpChannelsItem],
        FieldMetadata(alias="otpChannels"),
        pydantic.Field(alias="otpChannels", description="Channel to be used to deliver request OTP."),
    ]
    """
    Channel to be used to deliver request OTP.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
