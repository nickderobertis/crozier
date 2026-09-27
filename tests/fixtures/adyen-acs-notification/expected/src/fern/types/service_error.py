

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ServiceError(UniversalBaseModel):
    error_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="errorCode"),
        pydantic.Field(alias="errorCode", description="The error code mapped to the error message."),
    ] = None
    """
    The error code mapped to the error message.
    """

    error_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="errorType"),
        pydantic.Field(alias="errorType", description="The category of the error."),
    ] = None
    """
    The category of the error.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short explanation of the issue.
    """

    psp_reference: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pspReference"),
        pydantic.Field(alias="pspReference", description="The PSP reference of the payment."),
    ] = None
    """
    The PSP reference of the payment.
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    The HTTP response status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
