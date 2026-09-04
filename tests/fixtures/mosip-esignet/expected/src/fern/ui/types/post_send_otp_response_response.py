

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostSendOtpResponseResponse(UniversalBaseModel):
    """
    Successful message, or null if failed to deliver OTP.
    """

    transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionId"),
        pydantic.Field(alias="transactionId", description="oauth-details transactionId is used until the /token call."),
    ] = None
    """
    oauth-details transactionId is used until the /token call.
    """

    masked_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="maskedEmail"),
        pydantic.Field(alias="maskedEmail", description="Masked email id to which generated OTP was mailed."),
    ] = None
    """
    Masked email id to which generated OTP was mailed.
    """

    masked_mobile: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="maskedMobile"),
        pydantic.Field(alias="maskedMobile", description="Masked phone number to which generated OTP was messaged."),
    ] = None
    """
    Masked phone number to which generated OTP was messaged.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
