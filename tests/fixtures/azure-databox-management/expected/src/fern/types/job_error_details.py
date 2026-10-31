

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JobErrorDetails(UniversalBaseModel):
    """
    Job Error Details for providing the information and recommended action.
    """

    error_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="errorCode"),
        pydantic.Field(alias="errorCode", description="Code for the error."),
    ] = None
    """
    Code for the error.
    """

    error_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="errorMessage"),
        pydantic.Field(alias="errorMessage", description="Message for the error."),
    ] = None
    """
    Message for the error.
    """

    exception_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="exceptionMessage"),
        pydantic.Field(alias="exceptionMessage", description="Contains the non localized exception message"),
    ] = None
    """
    Contains the non localized exception message
    """

    recommended_action: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="recommendedAction"),
        pydantic.Field(alias="recommendedAction", description="Recommended action for the error."),
    ] = None
    """
    Recommended action for the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
