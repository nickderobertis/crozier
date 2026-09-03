

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_binding_otp_v2response_errors_item import PostBindingOtpV2ResponseErrorsItem
from .post_binding_otp_v2response_response import PostBindingOtpV2ResponseResponse


class PostBindingOtpV2Response(UniversalBaseModel):
    response_t_ime: typing_extensions.Annotated[
        str, FieldMetadata(alias="responseTIme"), pydantic.Field(alias="responseTIme")
    ]
    response: typing.Optional[PostBindingOtpV2ResponseResponse] = None
    errors: typing.Optional[typing.List[PostBindingOtpV2ResponseErrorsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
