

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_send_linked_otp_response_errors_item import PostSendLinkedOtpResponseErrorsItem
from .post_send_linked_otp_response_response import PostSendLinkedOtpResponseResponse


class PostSendLinkedOtpResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ] = None
    response: typing.Optional[PostSendLinkedOtpResponseResponse] = pydantic.Field(default=None)
    """
    Successful message, or null if failed to deliver OTP.
    """

    errors: typing.Optional[typing.List[PostSendLinkedOtpResponseErrorsItem]] = pydantic.Field(default=None)
    """
    List of Errors in case of request validation / processing failure in Idp server. if failure from IDA, the same error is relayed in this response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
