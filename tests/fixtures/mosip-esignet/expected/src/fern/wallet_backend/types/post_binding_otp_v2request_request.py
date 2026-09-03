

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostBindingOtpV2RequestRequest(UniversalBaseModel):
    individual_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="individualId"), pydantic.Field(alias="individualId", description="User Id (UIN/VID)")
    ]
    """
    User Id (UIN/VID)
    """

    otp_channels: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="otpChannels"),
        pydantic.Field(alias="otpChannels", description="Channels to which OTP should be delivered."),
    ]
    """
    Channels to which OTP should be delivered.
    """

    captcha_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="captchaToken"),
        pydantic.Field(alias="captchaToken", description="Captcha token, if enabled."),
    ] = None
    """
    Captcha token, if enabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
