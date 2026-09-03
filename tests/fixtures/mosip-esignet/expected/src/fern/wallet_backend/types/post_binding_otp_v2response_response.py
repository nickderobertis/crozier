

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostBindingOtpV2ResponseResponse(UniversalBaseModel):
    masked_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="maskedEmail"),
        pydantic.Field(alias="maskedEmail", description="Masked email id of the individualId user."),
    ] = None
    """
    Masked email id of the individualId user.
    """

    masked_mobile: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="maskedMobile"),
        pydantic.Field(alias="maskedMobile", description="Masked mobile number of the individualId user."),
    ] = None
    """
    Masked mobile number of the individualId user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
